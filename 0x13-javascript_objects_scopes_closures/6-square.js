#!/usr/bin/node

const Square = require('./5-square');

class ExtendedSquare extends Square {
  charprint(c) {
    const character = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}
module.exports = ExtendedSquare;
