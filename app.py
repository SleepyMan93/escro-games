import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/show_games")
def show_games():
    """
    Function to render the library of games on the library page
    """
    games = list(mongo.db.games.find())
    return render_template("games.html", games=games)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(403)
def no_entry(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403


@app.route("/library")
def library():
    games = list(mongo.db.games.find())
    return render_template("library.html", games=games)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    games = list(mongo.db.games.find({"$text": {"$search": query}}))
    return render_template("games.html", games=games)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "name": request.form.get("name").lower(),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("show_games", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    session["logged_in"] = True
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    games = list(mongo.db.games.find())

    if session.get('logged_in'):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, games=games)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/publish", methods=["GET", "POST"])
def publish():
    if request.method == "POST":
        game = {
            "genre_type": request.form.get("genre_type"),
            "game_title": request.form.get("game_title"),
            "game_description": request.form.get("game_description"),
            "price": request.form.get("price"),
            "dev_team": request.form.get("dev_team"),
            "image_link": request.form.get("image_link"),
            "release_date": request.form.get("release_date"),
            "created_by": session["user"]
        }
        mongo.db.games.insert_one(game)
        return redirect(url_for("show_games"))

    genres = mongo.db.genres.find().sort("genre_type", 1)
    return render_template("publish.html", genres=genres)


@app.route("/edit_post/<game_id>", methods=["GET", "POST"])
def edit_post(game_id):
    if 'user' in session:
        if session["user"]:
            if request.method == "POST":
                submit = {
                    "genre_type": request.form.get("genre_type"),
                    "game_title": request.form.get("game_title"),
                    "game_description": request.form.get("game_description"),
                    "price": request.form.get("price"),
                    "dev_team": request.form.get("dev_team"),
                    "image_link": request.form.get("image_link"),
                    "release_date": request.form.get("release_date"),
                    "created_by": session["user"]
                }
                mongo.db.games.update({"_id": ObjectId(game_id)}, submit)
    else:
        return render_template("403.html")

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    genres = mongo.db.genres.find().sort("genre_type", 1)
    return render_template("edit_post.html", game=game, genres=genres)


@app.route("/delete_post/<game_id>")
def delete_post(game_id):

    # check if user is logged in (session user)
    if 'user' in session:
        # checked logged in user against user of post or admin
        if session["user"]:
            # if conditions are met, delete post
            mongo.db.games.remove({"_id": ObjectId(game_id)})
    else:
        # else return error 403
        return render_template("403.html")

    return redirect(url_for("profile", username=session["user"]))


@app.route("/game_page/<game_id>", methods=["GET", "POST"])
def game_page(game_id):
    games = list(mongo.db.games.find())
    mongo.db.games.find({"_id": ObjectId(game_id)})

    return render_template("game_page.html", games=games)


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_type", 1))
    return render_template("genres.html", genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
