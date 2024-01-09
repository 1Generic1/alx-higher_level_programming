#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./countMoviesWithWedgeAntilles.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, filmsData) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Unexpected HTTP status code: ${response.statusCode}`);
  } else {
    const moviesWithWedgeAntilles = filmsData.results.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${moviesWithWedgeAntilles.length}`);
  }
});
