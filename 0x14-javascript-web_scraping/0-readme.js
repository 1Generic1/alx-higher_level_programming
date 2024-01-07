#!/usr/bin/node

const fs = require('fs');

function readAndPrintFileContent (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.log(error);
  }
}
if (process.argv.length !== 3) {
  console.error('Usage: ./readFile.js <file_path>');
  process.exit(1);
}
const filePath = process.argv[2];
readAndPrintFileContent(filePath);
