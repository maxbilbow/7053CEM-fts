$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/auth/register",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/user-profile";
    },
    error: function(resp) {
      var error = resp.responseJSON ? resp.responseJSON.error : "Unknown Error";
      $error.text(error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/auth/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/";
    },
    error: function(resp) {
      var error = resp.responseJSON ? resp.responseJSON.error : "Unknown Error"
      $error.text(error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});