#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length !== 4) {
  console.error('Usage: ./saveWebpage.js <url> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Unexpected HTTP status code: ${response.statusCode}`);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
