#!/usr/bin/node

const fs = require('fs');

function readAndPrintFileContent(filePath)
{
	try {
		const content = fs.readFileSync(filePath, 'utf-8');
		console.log(content);
	}
	catch (error) {
		if (error.code === 'EN0ENT') {
			console.error(`File not found: ${error.path}`);
		} else {
			console.error(`An error occurred: ${error.message}`);
		}
	}
}

if (process.argv.length !== 3) {
	console.error('Usage: ./readFile.js <file_path>');
	process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFileContent(filePath);
