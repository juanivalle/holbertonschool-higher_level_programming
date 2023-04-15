#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || isNaN(width) || isNaN(height)) {
      return undefined;
    } else {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
