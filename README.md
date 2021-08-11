Escro Games

#### Code Institute Full Stack Development Dipoloma: Milestone Project 3 - Backend Development
##### Created by William Donovan

![Project Displays](static/images/cover_photo)
[link to Project]()

# Table of Contents 

1. [UX Development](#uxdev)
   - Project Manifesto and Aim
   - User Goals
   - Designer Goals
   - Developer and Site Owner goals
   - User Stories 
   - Design Principles 
     * Fonts
     * Icons
     * Colours
     * Layout
   - Sitemap and Wireframes
   - Features and Future Implementations 
2. [Testing](#testing)
   - App Functionality Testing
      * Setting up Flask Environment
      * Connecting Flask with MongoDB
      * Python App Views
      * Life Cycle
   - HTML, CSS and Python checks
      * HTML
      * CSS
      * Python
   - User Testing
   - Manual Testing
3. [Bugs / De-bugging / Syntax Issues](#bugs)
4. [Technologies Used](#languages)
   - Languages Utilised
   - Online Material
   - Tools and Databases Used
5. [Project Deployment](#deployment)
   - Process of Deployment
   - How to create Local Version
6. [References](#references)
7. [Acknowledgements](#acknowledge)


# UX Development <a name="uxdev"></a>

## Project Manifesto and Aim 
"The UK video games market hit a record £7bn last year as lockdown fuelled an unprecedented boom in the popularity of mobile games, consoles and virtual reality headsets." A statement quoted from the Guardian roughly 6 months ago became the basis for Escro. With several major distribution services already available for PC and Console, I thought of creating an application, focusing around databse integration, for the new influx of gamer to post about and discover new Indie Games.  

The use of 'bumping' and 'commenting' will mirror the Reddit mechanic to hopefully create a community driven network. By storing all the data on MongoDB, the application can allow for searching, genre filtering, promotion of top posts and the ability to edit, delete and create posts within the app. The overall aim is tp utilise this new user base and generate coverage for new indpendent games.

## User Goals
The central target audience for this game is anyone with a passion for games but mainly between the ages of 14-35.

User Goals:
- Create an account
- Create, Read, Update and Delete content
- Publish posts about a game
- Comment on and 'bump' other user posts
- Search through the library of games with or without an account
- Check prices, platform and release availability

## Designer Goals
Hopefully the app will be useful for the games designers as well as the gamer.

Designer Goals:
- Create an account (possibly with designer privileges)
- Post about new releases and games not for release yet
- Users can search for production team and see what other releases they have
- Define a genre
- Simple but effective UX sheds some light on artwork and the games aesthetic 


## Developer and Site Owner Goals
Encourage new bedroom gamers to expand their horizons and be a part of the gaming community to help grow the space. 

Developer Goals:
- Create a functioning app for users that uses MongoDB to collect data. With this data, the Developer could understand gaming trends and other valuable knowledge about the industry.

# User Stories

- As a user, I want a profile feature so that I can manage my posts.
- As a games developer, I want to be able to search so that I can see if our catalogue is online yet.
- As the developer, I want a bump (upVote) feature so that I have alphanumeric data about each game.
- As a user, the ability to check the status of my post and see how successful it was via the upVotes.
- As a user and games developer, I want to be able to share information about games and find similar games myself.


# Design Principles

## Fonts

   
## Icons


## Colours


## Layout
For this project I will be trying out the Materialize Design Framework. It feels simialr to Bootstrap but the components seem to work better with the design layout the app is aiming to achieve.   
    
### Home Page
After initialising my functions and basic app inputs, the first deisgn layout decision I needed to make was how to layout the user posts. After searching through Materialize, I found a **Component** called **Collections** which seemlessly matched my initial Wireframe layout below. I used this as my template to inject the Jinja for loop that would fill the Component with the correct game content.
![Collections Component](static/images/collections_component.png)

Although this seemed like the best design choice, I actually ended up going with the Materialize table layout as my main structure. 
- INSERT PICTURE OF HOMEPAGE

I also decided on pushing over the main nav to the left and having a sidenav contain my logo and page links. The overall feel kept the context of the page more condensed and a more library aspect to my site.
- PIXTURE OF SIDENAV

# Sitemap / Wireframes



# Features / Future Implementations

- Eventually I would like to implement a feature that allows users to search for development teams or when the dev team is saved on Mongo, have the site create a dedicated
page for them and their releases.
- The ability to include notifiaction awareness for the user would be a great feature to have them coming back.
- Not really a difficult implementation but include the ability to purchse the game through our site or redirected to a place where that's possible.
- Include a more detailed 'relevancy' dropdown section on my Library page that allows sorting by: "Most Recent", "Most Popular", "Genre" etc

--------------------

# Testing <a name="testing"></a>

## App Functionality Testing

### **Setting up Flask environment**
- To initialise my Flask environment, app.py and env.py were created. Inside my env.py file, all the default environment variables needed to connect to Flask and the database "escro_games" on MongoDB. Below is a screenshot of my app.py initialisation, when run for the first time, it was unsuccessful due to a syntax error...  

_After changing "is" to "if", my test function produced "Hello World!" on the test site. Flask is now successfully initialised and working_
![Syntax Error](static/images/syntax_error_app_test.png)  

### **Connecting Flask with MongoDB**
- After installing frameworks **flask-pymongo** and **dnspython** and importing them into the app, I created a simple app function that would populate **game.html** with the **values** from the **games** collection on MongoDB. 
![Connection Function](static/images/test_connection_function.png)  

- Plugging in an instance of Mongo using the app instance of python, I was able to create an app function **show_games**. The function stores the data from the **games** collection in a new Python variable called **games**. Using the Flask function **render-template**, the data stored in **games** can be output to a file location **games.html**, using Jinja.  

- After populating the **games.html** file using **html:5** boilerplate tab, the file needs to loop through each game within the collection to dsiplay it on site. Using the new variable **game**, which now holds all the data, applying dot notation, Jinja can target each field and render it to the HTML and preview site...
![Jinja Data Test](static/images/jinja_template_test.png)  

- My test function produced no errors or bugs and so the connection between Flask and Mongo was successful...
![Test Connection Preview](static/images/mongo_db_data.png)    

### **Python App Views**
- All my app views for CRUD worked with no isses except for the UPDATE stage. I encountered most of my issues with this part of the app functionality.
The most important error that I had to fix when testing the final app was submitting the users changes. Initially when the "Submit" button was pressed, the page would 
only reload and the data was not updated. EVentually I found that and the "delete" function shared a similar issue. The IDs I had used to target the inputs and buttons were
used twice accross the "publish" page and the "edit" page because they had the same boiler plate. Once I made the IDs unique, the information was deleted and updated correctly

- Once my basic CRUD functionality was in place, the aim was to redesign the app direction so that on the users profile they could only see their posts. At first I wasn't able to even get the game list to render in but realised I was trying to load the list in the wrong view...
![User Game Function](static/images/user_game_function.png)     

Above is what my app view looked like to try and find game documents associated with the user that was logged in. Through tracing the redirects, I realised the list needed to be loaded into the profile view. Now the list of games load but need to try and work out how to remove other users posts...    

The solution wasn't found in creating another app view but simply an error in forgetting **|lower** in my Jinja forloop:

![Profile Only Post](static/images/profile_only_post.png)

- A similar error was occuring when trying to Edit and Delete posts. Now the Profile page loaded only the specific user's posts, with all the correct information injected into the table. However, the buttons, even though correctly taking you to the edit page or deleting the post, only the first game document would be affected. 

- With all my functions for CRUD working, I wanted to put some defensive programming into the app which stops people from forcing their way onto profiles and deleting posts that are not their property. My first stage was to make sure the session['user'] was session['logged_in']. To check this, I put an **if** condition in my profile view that when the user logs in, if session['logged_in'] == True, a flash message would appear....
![Session Logged In Check](static/images/session_logged_in_check.png)    

SUCCESS! Once the user had logged in and was taken to the profile page, the flash message was produced...   
![Logged In Flash](static/images/logged_in_flash.png)

From here, after several tests, I simply had to ask if the user was logged in. If so, is the user the same user as the game.created_by and if that condition is met, the game could be deleted or edited. I produced the else statement in line with, if there was no user.session.logged_in, then the app would redirect to the error403 (forbidden) page...
![Defensive Programming Edit](static/images/defensive_programming_edit.png)    
![Defensive Programming Delete](static/images/defensive_programming_delete.png)

## Life Cycle

 - Below is a screenshot of the very early skeleton for my site. The **fixed side-nav** in place which is main design feature for my app. Basic **Jinja**, **Flask** and **Python** functionality in place:   

![Test Connection Preview](static/images/site_skeleton.png)

 - Added in registration page that successfully grabs user data from the inputs and stores correctly in the 'users' collection within the database:   

![Test Connection Preview](static/images/successful_reg.png)
![Test Connection Preview](static/images/user_data.png)

 - Unpacked my first listed game data into the **Collections Component** from Materialize. Home page basic structure beginning to take form:   

![Basic Home Page](static/images/basic_homepage.png)   

 - Created basic the boilerplate for the user to publish a post with all the inputs ready to fill results for the game document:    

![Publish Boilerplate](static/images/publish_boilerplate.png)


## HTML CSS and Python validation checks

### HTML
* [HTML Validator](https://validator.w3.org/) was used to validate. I copied out each page source and ran through the validator. My main problem was when looping in Jinja, IDs were replicated for each instance. Went back and used classes instead. Very few errors except random non closure of divs / li which are not present.
### CSS
* [CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate. No errors were found. I received a CSS + Level 3 SVG.    
![CSS Validation Certificate](static/images/css_validation.png)
### Python
* [PEP8](http://pep8online.com/) was used to validate. No errors found.
![PEP8 Validation](static/images/pep8_validation.png)


## User Testing 

- Tested delete and edit button on the profile page as user. The button appeared to work for edit, taking me to the correct boilerplate and app view but the delete
function would only delete the first game document for that user. 

- Tried testing all the CRUD functionalites as a user. Everything worked apart from the UPDATE part. When I went to submit my edit, the page simply reloaded and 
nothing had changed. 

- Attempted search function as user which works apart from when searching for a title. The search only worked if the complete title was entered which for the user
isn't very convienient. Instead, I added in a search index which allows users to search for words in the game.description which should help with producing "No Results Found"

## Manual Testing

✔️ Navigation links: All redirect to the correct pages.

✔️ Footer links: All redirect to the correct pages.

✔️ Try deleting Posts when not logged in: A 403 error page appears asking user to log in/register.

✔️ Try loading an unrecognised link page: A 404 error page appears sending the user back to the homepage.

✔️ Submit registration form with a user/email that already exists in database: User is prevented from signingin. A flash message is produced stating the username already exists.

✔️ Submit registration form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit registration form with a new user/email that doesn't exist in database: Successfully sends user data to MongoDB and redirects user to the Home page. 

✔️ Submit Log In form if no username exists in database that matches entered username: Error message appears stating incorrect username and/or password.

✔️ Submit Log In form if username is correct but password doesn't match: User is prevented from signing in. An Error message appears stating incorrect username and/or password.

✔️ Submit Log In form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit log in form with correct username and password: Starts session and takes user to the Home page. 

✔️ Press the Sign Out button when logged in: Ends the session and sends user back to login.html. 

✔️ Try adding a post when logged in: Successfully creates a post and redirects user to their Profile page only if all the fields are filled in correctly. 

✔️ Try editing a post on the My Account page: Successfully renders in original game information, updates post and renders the new information on the edit page only if all the fields are filled in correctly. If not, an error message appears.

✔️ Try deleting a post while on the Profile page: User successfully deletes post and is taken back to their profile with the post removed

✔️ Search posts on site: If results found, post is rendered on the home page. If no results, message stating no results found and a return to home page button produced. 

✔️ Try logging in with the credentials from the deleted account: Get an error message. 


# Bugs / De-Bugging / Syntax Issues<a name="bugs"></a>

## Errors

The first error encountered was during the initialisation of my **base.html** page. After importing **Materialize**, **JS** and **Font Awesome** script / link tags, my test site produced a Jinja syntax error...   

![Jinja Syntax Error](static/images/jinja_syntax.png)
![Jinja Issue](static/images/jinja_error.png)  

    RESOLVED: _Upon inspecting the **base.html** template, the reason for the error was found in the **scripts** section. I forgot to close the **Block** tag which was prevnting the template from loading._

## Bugs

I encountered my first bug once the **fixed side-nav** was in place. For some reason the **anchor** links were displaying above the **text** for that page link. The links worked but had no text inside... 

![Li Text Bug](static/images/li_bug.png)   

    DE-BUGGED: In the exmaple above, you can see through DevTools, the issue was due to HTML formatting. For some reason I placed the text inside the li tag and therefore it was displaying below. A simple fix, put the text inside the a tag.

Found a bug with my flash messages. After creating a successful Python function that **POSTS** the Registration data to my DB, a flash message is produced. However, the message flashed seems to be in a list format, being wrapped in **[' ']**...   

![Flash Message Bug](static/images/flash_message_bug.png)   

    DE-BUGGED: The issue was arriving from my Jinja for-loop in base.html. Inside the div that holds the flashed message from messages, I put {{ messages}} plural, rather than {{ message }} singular. This was creating the list format style. 

A bug occured when trying to inject the **game** list items into the **Collections** Component template from Materialize. The component template appeared as a white line once I tried to unpack the neccessary game data into it...   

![Jinja ForLoop Bug](static/images/jinja_for_loop_bug.png)   

    DE_BUGGED: After reading back through my notes from the mini-project, I found that in my app.show_games view, the list was technically a Mongo Cursor Object. By turning it into a proper list, the game items were unpacked properly.   
![Jinja ForLoop Fix](static/images/jinja_for_loop_fix.png)   

Encountered a fairly annoying bug that saw my Game **genre** options not being posted to the database. Everything else wrapped inside the "POST" form was successfully posting bar the genre choice. The dropdown would "GET" the **genre_type** options but not "POST" them with everything else...   

![Genre Post Bug](static/images/genre_post_bug.png)    

    DE_BUGGED: After checking through the stages, I realised that the genre was in fact posting to the database but just not being displayed properly through the Jinja template. In the end, quite a simple fix. Just had to ammend the "game.genre" call to "game.genre_type" as I changed the name half way through the development.     
![Genre Post Fix](static/images/genre_post_fix.png)    

I ran into this bug that would force the game post content up and under the nav bar. The new dropdown button to edit the post, only the last in the list however, was causing this to happen...    
![Dropdown Bug](static/images/dropdown_bug.png)    

    DE-BUGGED: I managed to solve the issue using Dev Tools. The Materialize CSS was setting the UL of class="collection" to Overflow: Hidden which was forcing the content to fit inside the container. I just created my own custom style and applied overflow: visible to fix.

When styling the app, I encountered a bug regarding the **Profile** page. It was the only template that didn't render in the logo but extended everything else from the **base.html** boilerplate...     
![Profile Logo Bug](static/images/no_logo_admin_bug.png)

    DE_BUGGED: The issue was a fairly simple one. I forgot to include the forward slash before "static/images.." in my base.html template. Thus the link wasn't coming from the root and not rendering properly.    

Encountered a bug when trying to upload and edit posts. All the game credentials show on the page bar the image... 
![Image Bug](static/images/image_bug.png)   

    DE-BUGGED: The issue was originating from my "edit" and "publish" app views. The extra dictionary insert that uploaded the image link to the Mongo document was missing. 


# Technologies Used <a name="languages"></a>

1. [jQuery](https://jquery.com/)
2. [Materialize](https://https://materializecss.com/)
3. [CSS 4](https://www.w3schools.com/w3css/)
5. [HTML 5](https://en.wikipedia.org/wiki/HTML5)
6. [JavaScript](https://www.javascript.com/)
7. [Dev Tools](http://ami.responsivedesign.is/)
8. [jQuery](https://jquery.com/)
9. [Python](https://www.python.org/)
10. [MongoDB](https://www.mongodb.com/)
11. [Heroku](https://heroku.com)
12. [Flask](https://flask.palletsprojects.com/en/2.0.x/)

# Project Deployment <a name="deployment"></a>
## Process of deployment

#### Heroku:  

1. _For the Heroku app to successfully understand what **Framework Requirements** and Python applications to run, a **Procfile** and **requirements.txt** are a must..._  

Using the command **pip3 freeze --local > requirements.txt** in the terminal will create a requirements.txt file with all the dependencies listed to run the Heroku App. Whenever new packages are installed, remeber to update the .txt file | Using the command **echo web: python app.py > Procfile** in ther terminal will create a Procfile, which Heroku uses to know which Python App to run when the site is loaded.  

2. _After initial set up of the Flask app, our next step is to get Heroku to update, recognise and connect with our site..._  

To do this, you need to make an account on Heroku, upon signing in, click **New** to create the app. On the next screen, produce a name for the app, making sure to use lowercase and the region closest to you. If the domain name is available, finish by clicking **Create App**.  

3. _Next we need to have our code update on Heroku automatically. The easiest way to do this is linking the sites repo in Github with the Heroku app..._  

Navigate to the **Deploy** tab and choose **github** as the **Deployment Menthod**. Sign in and Search for the repo name. Once found, choose **connect**.  

4. _Due to the fact we have hidden KEY Environment Variables in the **env.py** file, that Heroku won't be able to retrieve from the **GitHub Repo**, we need to store this in Herkou's **Config Vars**..._  

Under the settings tab you will find the **Config Vars** section. Reveal the section and copy all the **KEY** and **VALUE** pairs from the **env.py** file. Making sure not to include any of the **quotation marks**.  

5. _For the last stage, it is key to make sure the **requirements.txt** and **Procfile** are pushed to the GitHub Repo..._   

Once these files are successfully pushed to GitHub, make sure to **Enable Automatic Deploy**. You can then click **Deploy Branch**, generally **main** or **master**. The Heroku app will take a few minutes to set up the connection. Once successful, every commit pushed to GitHub will update the Heroku app and Live Site.

## How to create Local Version

#### Clone the repository and run locally:

1. Navigate to the repository from the Github Dashboard
1. Select the green button in the top right of the screen that says "Clone or download"
1. Click on the clipboard icon to the right of the URL to copy it
1. Open an Integrated Development Environment (IDE) and head over to the terminal
1. Change the directory to where you want to clone the repository to
1. Execute the following command by pasting in the URL you copied in step 3: git clone https://github.com/debrawolford/treat-your-pup.git
1. Press Enter
1. The site will then be cloned
1. Install all the project dependencies by typing `pip install -r requirements.txt`

#### Set Up Environment Variables:

1. Create an env.py file in your root directory.
1. Add env.py file to the.gitignore file.
1. Add the following to your env.py file with the applicable variables: 
```
import os
os.environ["MONGO_URI"] = "mongodb+srv://username:password@myfirstcluster-strtg.mongodb.net/plant_swap?retryWrites=true&w=majority"
os.environ["IP"] = "0.0.0.0"
os.environ["PORT"] = "5000"
os.environ["SECRET_KEY"] = "Your Secret Key"
```

[Back to Top](#table-of-contents)


# References <a name="references"></a>
- Aside from StackOverflow [StackOverflow]

# Acknowledgements <a name="acknowledge"></a>




