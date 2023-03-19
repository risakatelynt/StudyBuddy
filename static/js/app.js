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
            window.location.href = "http://127.0.0.1:8000/notes";
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
      $(".container").addClass("opacity");
      $(".spinner-border").show();
      $.ajaxSetup({
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
      });
      $.ajax({
        type: "POST", // http method
        data: {
          username: $("#username").val(),
          password: $("#password").val(),
          // csrfmiddlewaretoken: csrf_token
        }, // data sent with the post request
        dataType: "json",
        // handle a successful response
        success: function (json) {
          console.log(json); // log the returned json to the console
          if (json.response && json.response == "success") {
            window.location.href = "http://127.0.0.1:8000/notes";
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
      // form.submit();
      //   // window.location = "notes";
    },
  });

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
});
