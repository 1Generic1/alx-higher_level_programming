#!/usr/bin/node

const data = require('./101-data').dict;
const occurrencesDict = Object.keys(data).reduce((result, userId) => {
  const occurrences = data[userId];
  if (!result[occurrences]) {
    result[occurrences] = [userId];
  } else {
    result[occurrences].push(userId);
  }
  return result;
}, {});
console.log(occurrencesDict);
