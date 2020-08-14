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
  //   materialize select dropdown
  $("select").formSelect();
});
