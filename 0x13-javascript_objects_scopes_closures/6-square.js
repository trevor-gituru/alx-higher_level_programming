#!/usr/bin/node
// Task 6
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (typeof c !== 'string') {
      c = 'X';
    }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.width; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
