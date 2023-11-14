#!/usr/bin/node
const args = process.argv.slice(2);
const integers = args.map(arg => parseInt(arg));
const sortedIntegers = integers.sort((a, b) => b - a);
const secondBiggest = sortedIntegers[1] || 0;
console.log(secondBiggest);
