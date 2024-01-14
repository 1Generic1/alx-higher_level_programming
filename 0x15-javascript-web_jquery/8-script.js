// Wait for the DOM to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch movie data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            // Check if data contains results
            if (data.results) {
                // Select the UL with ID 'list_movies'
                let listMovies = $('#list_movies');

                // Loop through each movie result and append a new LI to the UL
                $.each(data.results, function(index, movie) {
                    listMovies.append('<li>' + movie.title + '</li>');
                });
            } else {
                console.error('No movie data found.');
            }
        },
        error: function() {
            console.error('Error fetching movie data.');
        }
    });
});

