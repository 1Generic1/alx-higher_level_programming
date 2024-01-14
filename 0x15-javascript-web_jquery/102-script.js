$(document).ready(function() {
  // Handle click event on the button
  $('#btn_translate').on('click', function() {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX request to the API
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: languageCode },
      success: function(data) {
        // Update the content of the HTML tag with the fetched translation
        $('#hello').text(data.hello);
      },
      error: function() {
        console.error('Error fetching translation.');
      }
    });
  });
});
