#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./getMovieTitle.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Unexpected HTTP status code: ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(`Title: ${movieData.title}`);
    } catch (parseError) {
      console.log(`Error parsing JSON response: ${parseError.message}`);
    }
  }
});
