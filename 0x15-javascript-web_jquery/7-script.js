$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      $('#character').text(data.name);
    },
    error: function() {
      console.error('Error fetching data from the API');
    }
  });
});
