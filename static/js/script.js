$(document).ready(function () {
  $('.sidenav').sidenav();
  $('select').formSelect();
  $('.dropdown-trigger').dropdown({closeOnClick: "true"});
  $('.fixed-action-btn').floatingActionButton();
  $('.datepicker').datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 5,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  });

  var i = 0;
  upPump()
  function upClick() {
      i++;
      document.getElementById('inc').value = i;
  };

  downDump()
  function downDump() {
      i++;
      document.getElementById('inc').value = i;
  };
});
