$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (translate) {
    $('#hello').html(translate.hello);
  });
});
