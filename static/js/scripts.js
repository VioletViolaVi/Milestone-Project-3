$(document).ready(function () {
  // materialize sidenav
  $(".sidenav").sidenav();
  // materialize carousel
  $(".carousel.carousel-slider").carousel({
    fullWidth: true,
    indicators: true,
    duration: 250,
  });
  // materialize modal
  $(".modal").modal();
  // materialize select dropdown
  $("select").formSelect();
  // materialize datepicker
  $(".datepicker").datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 5,
    showClearBtn: true,
    firstDay: 1,
    i18n: {
      done: "Select",
    },
  });
});
