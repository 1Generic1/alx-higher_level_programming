#!/usr/bin/node

const myList = require('./100-data').list;
const newArray = myList.map((value, index) => value * index);
console.log(myList);
console.log(newArray);
