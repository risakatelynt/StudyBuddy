$(document).ready(function () {
  // hide spinner
  setTimeout(function () {
    $(".spinner-border").hide();
    $(".container").removeClass("opacity");
    $(".content").removeClass("opacity");
  }, 1000);
  //show or hide password
  $("#toggle-password").click(function () {
    $("#toggle-password").toggleClass("fa-eye fa-eye-slash");
    if ($(this).hasClass("fa-eye")) {
      $("#password").attr("type", "text");
    } else {
      $("#password").attr("type", "password");
    }
  });
  //show or hide password
  $("#toggle-reenter-password").click(function () {
    $("#toggle-reenter-password").toggleClass("fa-eye fa-eye-slash");
    if ($(this).hasClass("fa-eye")) {
      $("#password2").attr("type", "text");
    } else {
      $("#password2").attr("type", "password");
    }
  });
  var username;
  // validate signup form
  $(".signin-form").validate({
    rules: {
      username: {
        required: true,
      },
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true,
        minlength: 6,
      },
      password2: {
        required: true,
        minlength: 6,
      },
    },
    messages: {
      username: "Username is required",
      email: "Email is required",
      password: {
        required: "Password is required",
        minlength: "Please enter minimum 6 characters",
      },
      password2: {
        required: "Password is required",
        minlength: "Please enter minimum 6 characters",
      },
    },
    submitHandler: function (form) {
      username = $("#username").val();
      sessionStorage.setItem("username", username);
      $(".container").addClass("opacity");
      $(".spinner-border").show();
      $.ajaxSetup({
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
      });
      $.ajax({
        url: "", // the endpoint
        type: "POST", // http method
        data: {
          username: $("#username").val(),
          email: $("#email").val(),
          password: $("#password").val(),
          password2: $("#password2").val(),
          // csrfmiddlewaretoken: csrf_token
        }, // data sent with the post request
        dataType: "json",
        // handle a successful response
        success: function (json) {
          console.log(json); // log the returned json to the console
          if (json.response && json.response == "success") {
            window.location.href = "/notes/";
          } else if (json.response && json.response.message) {
            $("#results").text(json.response.message);
          }
          setTimeout(function () {
            $(".spinner-border").hide();
            $(".container").removeClass("opacity");
          }, 1000);
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
          console.log(errmsg);
          setTimeout(function () {
            $(".spinner-border").hide();
            $(".container").removeClass("opacity");
          }, 1000);
        },
      });
    },
  });

  $("#login-form").validate({
    rules: {
      username: {
        required: true,
      },
      password: {
        required: true,
      },
    },
    messages: {
      username: "Username is required",
      password: {
        required: "Password is required",
      },
    },
    submitHandler: function (form) {
      console.log("form submitted!"); // sanity check
      username = $("#username").val();
      sessionStorage.setItem("username", username);
      $(".container").addClass("opacity");
      $(".spinner-border").show();
      $.ajaxSetup({
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
      });
      $.ajax({
        type: "POST",
        data: {
          username: $("#username").val(),
          password: $("#password").val(),
        },
        dataType: "json",
        // handle a successful response
        success: function (json) {
          if (json.response && json.response == "success") {
            window.location.href = "/notes/";
          } else if (json.response && json.response.message) {
            $("#results").text(json.response.message);
          }
          setTimeout(function () {
            $(".spinner-border").hide();
            $(".container").removeClass("opacity");
          }, 1000);
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
          console.log(errmsg);
          setTimeout(function () {
            $(".spinner-border").hide();
            $(".container").removeClass("opacity");
          }, 1000);
        },
      });
    },
  });
  var notesList;
  if (top.location.pathname === "/notes/") {
  username = sessionStorage.getItem("username");
    $("#userId").append(username);
    $.ajax({
      url: "http://127.0.0.1:8000/note/",
      type: "GET",
      dataType: "json",
      // handle a successful response
      success: function (json) {
        if (json.response) {
          console.log(json);
          notesList = json.response;
          var count = 0;
          json.response.forEach((item, j) => {
            $(
              '<div class="row mb-5 py-3 bg-green" id="card' +
                j +
                '"><img class="col-5 col-md-3 card-img-top" src="' +
                item.image +
                '"><div class="col-7 col-md-9 px-0"><div id="edit' +
                j +
                '"><h5 class="col-12">' +
                item.title +
                '</h5><p class="col-12 card-text">' +
                item.content +
                "</p></div>" +
                '<div class="col-12 my-3 stars-rating' +
                j +
                '">' +
                '<span class="size-16 pl-3">' +
                item.rank +
                "</span></div>" +
                '<div class="col-12">' +
                '<button id="' +
                j +
                '" type="button" class="btn btn-dark float-end" data-toggle="modal" data-target="#myModal">Details</button></div>' +
                "</div></div>"
            ).appendTo(".notesList");
          });
          json.response.forEach((mainItem, index) => {
            var stars = mainItem.rank;
            for (let k = 0; k < stars; k++) {
              $('<span class="fa fa-star checked"></span>').prependTo(
                ".stars-rating" + index
              );
            }
          });
          $(".carousel-item").first().addClass("active");
          $(".carousel-indicators > li").first().addClass("active");
          $("#carousel-example-generic").carousel();
          for (let k = 0; k < json.response.length; k++) {
            $(".hide-save" + k).hide();
          }
        } else if (json.response && json.response.message) {
          console.log(json.response.message);
        }
        setTimeout(function () {
          $(".spinner-border").hide();
          $(".container").removeClass("opacity");
        }, 1000);
      },

      // handle a non-successful response
      error: function (xhr, errmsg, err) {
        console.log(errmsg);
        setTimeout(function () {
          $(".spinner-border").hide();
          $(".container").removeClass("opacity");
        }, 1000);
      },
    });
    console.log(username, $("#username").val());
  }

  // Show the first tab and hide the rest
  $("#tabs-nav li:nth-child(2)").addClass("active");
  $(".tab-pane").hide();
  $(".tab-pane:nth-child(2)").show();

  // tabs click function
  $("#tabs-nav li").click(function () {
    $("#tabs-nav li").removeClass("active");
    $(this).addClass("active");
    $(".tab-pane").hide();

    var activeTab = $(this).find("a").attr("href");
    $(activeTab).fadeIn();
    return false;
  });

  // questions table
  $("#myTable").dataTable({
    fnDrawCallback: function (oSettings) {
      var previousPageEl = document.querySelector("#myTable_previous");
      previousPageEl.innerHTML = "";
      $(".paginate_button.previous").append('<i class="fa fa-angle-left"></i>');
      var nextPageEl = document.querySelector("#myTable_next");
      nextPageEl.innerHTML = "";
      $(".paginate_button.next").append('<i class="fa fa-angle-right"></i>');

      $(".paginate_button").append(
        '<i class="fa fa-bolt" aria-hidden="true"></i>'
      );

      var queue = document.getElementsByClassName("previous");
      var elements = queue[0].getElementsByTagName("i");
      queue[0].removeChild(elements[1]);
      var queue = document.getElementsByClassName("next");
      var elements = queue[0].getElementsByTagName("i");
      queue[0].removeChild(elements[1]);
    },
  });

  $("#myTable_info").hide();
  $("#myTable_filter label").append(
    '<span class="fa fa-search form-control-feedback"></span>'
  );

  // on click of details button of notes page
  // $(".float-end").click(function () {
  //   console.log(this);
  //   var id = $(this).attr("id");
  //   var carousel = $(this).parent().closest(".bg-green");
  //   if (carousel) {
  //     var imgEl = carousel.find("img")[0];
  //     var cardsEl = carousel.find(".card-text");
  //     $("#myModal img").attr("src", imgEl.src);
  //     var headerText = cardsEl[0].innerHTML;
  //     headerText = headerText
  //       .replace("\n", "")
  //       .replace(/\s{2,}/g, " ")
  //       .trim();
  //     var contentText = cardsEl[1].innerHTML;
  //     contentText = contentText
  //       .replace("\n", "")
  //       .replace(/\s{2,}/g, " ")
  //       .trim();
  //     $(".modal-textarea").text(headerText);
  //     $(".modal-textarea").append("\n");
  //     $(".modal-textarea").append(contentText);
  //   }
  // });
  var ratingValue = $("#rating-number").val();
  $(".modal-textarea").attr("disabled", true);
  $(".input-header").attr("disabled", true);
  var textareaData;
  $(".hide-edit").show();
  $(".hide-save").hide();
  var id = -1;
  $(".notesList").on("click", ".float-end", function () {
    textareaData = $(".modal-textarea").val();
    id = $(this).attr("id");
    $("#myModal img").attr("src", notesList[id].image);
    $(".input-header").val(notesList[id].title);
    $(".modal-textarea").text(notesList[id].content);
    var stars = $("#stars li.star");
    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass("selected");
    }
    for (i = 0; i < notesList[id].rank; i++) {
      $(stars[i]).addClass("selected");
    }
  });
  $("#edit-btn").click(function () {
    $(".hide-edit").hide();
    $(".hide-save").show();
    $(".input-header").attr("disabled", false);
    $(".modal-textarea").attr("disabled", false);
    $("#stars").removeClass("disabled");
  });
  $("#save-btn").click(function () {
    $(".spinner-border").show();
    notesList[id].title = $(".input-header").val();
    notesList[id].content = $(".modal-textarea").val();
    $(".input-header").attr("disabled", true);
    $(".modal-textarea").attr("disabled", true);
    $("#stars").addClass("disabled");
    $(".hide-edit").show();
    $(".hide-save").hide();

    // $.ajaxSetup({
    //   headers: {
    //     "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
    //       .value,
    //   },
    // });
    // $.ajax({
    //   url: `http://127.0.0.1:8000/updatenotes/${id}`,
    //   type: "POST",
    //   data: {
    //     id: id,
    //     topic: notesList[id].title,
    //     name: "",
    //     description: notesList[id].content
    //   },
    //   dataType: "json",
    //   // handle a successful response
    //   success: function (json) {
    //     if (json.response && json.response == "success") {
    //       console.log(json);
    //     } else if (json.response && json.response.message) {
    //       console.log(json.response.message);
    //     }
    setTimeout(function () {
      $(".spinner-border").hide();
      $(".container").removeClass("opacity");
    }, 2000);
    //   },

    //   // handle a non-successful response
    //   error: function (xhr, errmsg, err) {
    //     console.log(errmsg);
    //     setTimeout(function () {
    //       $(".spinner-border").hide();
    //       $(".container").removeClass("opacity");
    //     }, 1000);
    //   },
    // });
  });
  $("#cancel-btn").on("click", function () {
    $(".input-header").val(notesList[id].title);
    $(".modal-textarea").val(notesList[id].content);
    $("#rating-number").text(notesList[id].rank);
    $(".hide-edit").show();
    $(".hide-save").hide();
    $(".input-header").attr("disabled", true);
    $(".modal-textarea").attr("disabled", true);
    var stars = $("#stars li.star");
    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass("selected");
    }
    for (i = 0; i < notesList[id].rank; i++) {
      $(stars[i]).addClass("selected");
    }
    $("#stars").addClass("disabled");
  });

  $(".close").click(function () {
    console.log("dsfas");
  });

  $("#stars").addClass("disabled");
  $("#stars li")
    .on("mouseover", function () {
      var onStar = parseInt($(this).data("value"), 10);

      // Now highlight the stars
      $(this)
        .parent()
        .children("li.star")
        .each(function (e) {
          if (e < onStar) {
            $(this).addClass("hover");
          } else {
            $(this).removeClass("hover");
          }
        });
    })
    .on("mouseout", function () {
      $(this)
        .parent()
        .children("li.star")
        .each(function (e) {
          $(this).removeClass("hover");
        });
    });

  /* Action to perform on click of stars */
  $("#stars li").on("click", function () {
    var onStar = parseInt($(this).data("value"), 10); // The star currently selected
    var stars = $(this).parent().children("li.star");

    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass("selected");
    }

    for (i = 0; i < onStar; i++) {
      $(stars[i]).addClass("selected");
    }

    var newRatingValue = parseInt(
      $("#stars li.selected").last().data("value"),
      10
    );
    $("#rating-number").text(newRatingValue);
  });
});
