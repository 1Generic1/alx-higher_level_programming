$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    translateHello();
  });
  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
        translateHello();
    }
  });
  function translateHello() {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      success: function (data) {
          $('#hello').text(data.hello);
      },
      error: function () {
          $('#hello').text('Translation not available');
      }
    });
  }
});

