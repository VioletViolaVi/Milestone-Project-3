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
    yearRange: 3,
    showClearBtn: true,
    firstDay: 1,
    i18n: {
      done: "Select",
    },
  });


$(function () {
 
  $("#rateYo").rateYo({
    rating: 2,
    fullStar: true
  });
});

// Getter
var normalFill = $("#rateYo").rateYo("option", "fullStar"); //returns true
 
// Setter
$("#rateYo").rateYo("option", "fullStar", true); //returns a jQuery Element




  // from code institute 
//   validateMaterializeSelect();
//   function validateMaterializeSelect() {
//     if ($("select").prop("required")) {
//       $("select").css({
//         display: "block",
//         height: "0",
//         padding: "0",
//         width: "0",
//         position: "absolute",
//       });
//     }
//   }
//   $(".select-wrapper input.select-dropdown")
//     .on("focusin", function () {
//       $(this)
//         .parent(".select-wrapper")
//         .on("change", function () {
//           if (
//             $(this)
//               .children("ul")
//               .children("li.selected:not(.disabled)")
//               .on("click", function () {})
//           ) {
//             $(this).children("input");
//           }
//         });
//     })
//     .on("click", function () {
//       if (
//         $(this)
//           .parent(".select-wrapper")
//           .children("ul")
//           .children("li.selected:not(.disabled)")
//       ) {
//         $(this).parent(".select-wrapper").children("input");
//       } else {
//         $(".select-wrapper input.select-dropdown").on("focusout", function () {
//           if (
//             $(this)
//               .parent(".select-wrapper")
//               .children("select")
//               .prop("required")
//           ) {
//           }
//         });
//       }
//     });


});
