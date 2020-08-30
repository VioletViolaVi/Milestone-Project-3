$(document).ready(function () {
  // materialize sidenav
  $(".sidenav").sidenav();
  // materialize modal
  $(".modal").modal();
  // materialize select dropdown
  $("select").formSelect();
  // materialize datepicker
  $(".datepicker").datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 3,
    showClearBtn: true,
    firstDay: 1,
    i18n: {
      done: "Select",
    },
  });
  // materialize carousel
  $(".carousel").carousel({
    dist: 0,
    duration: 500,
    padding: 200,
    numVisible: 6,
    fullWidth: true,
    indicators: true,
    noWrap: false,
  });
});
