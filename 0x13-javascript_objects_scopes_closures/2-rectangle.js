#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      Object.defineProperty(this, 'w', { value: undefined, enumurable: false });
      Object.defineProperty(this, 'h', { value: undefined, enumerable: false });
    }
  }
}
module.exports = Rectangle;
