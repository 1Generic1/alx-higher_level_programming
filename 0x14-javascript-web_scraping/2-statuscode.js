#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./getStatus.js <url>');
  process.exit(1);
}
const url = process.argv[2];
request(url, (error, response) => {
  if (error) {
    console.log(`Error: ${error.message}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
