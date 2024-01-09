#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./printMovieCharacters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Unexpected HTTP status code: ${response.statusCode}`);
  } else {
    const data = JSON.parse(body);
    const dd = data.characters;
    for (const i in dd) {
      const characterUrl = dd[i];
      request.get(characterUrl, (error, response, body1) => {
        if (error) {
          console.log(error);
        }
        const data1 = JSON.parse(body1);
        console.log(`${data1.name}`);
      });
    }
  }
});
