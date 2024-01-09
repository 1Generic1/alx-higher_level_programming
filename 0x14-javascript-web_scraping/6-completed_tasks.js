#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./countCompletedTasks.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, todos) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Unexpected HTTP status code: ${response.statusCode}`);
  } else {
    const completedTasks = todos.filter(todo => todo.completed);
    const completedTasksByUser = {};
    completedTasks.forEach(todo => {
      if (!completedTasksByUser[todo.userId]) {
       completedTasksByUser[todo.userId] = 1;
      } else {
	completedTasksByUser[todo.userId]++;
      }
  });
  console.log(JSON.stringify(completedTasksByUser, null, 2));
  }
 });
