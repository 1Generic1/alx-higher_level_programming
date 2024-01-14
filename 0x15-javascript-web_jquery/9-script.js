// Ensure that the script runs after the DOM is ready
$(document).ready(function() {
    // Make an AJAX request to fetch the translation
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: function(data) {
            // Update the content of DIV#hello with the fetched translation
            $('#hello').text(data.hello);
        },
        error: function() {
            // Handle errors if needed
            console.error('Failed to fetch translation.');
        }
    });
});
