#!/usr/bin/node

const fs = require('fs');

function writeToFile (filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf-8');
  } catch (error) {
    console.log(error);
  }
}
if (process.argv.length !== 4) {
  console.error('Usage: ./writeFile.js <file_path> <content>');
  process.exit(1);
}
const filePath = process.argv[2];
const content = process.argv[3];
writeToFile(filePath, content);
