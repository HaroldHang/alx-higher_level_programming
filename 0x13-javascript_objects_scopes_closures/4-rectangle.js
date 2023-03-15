#!/usr/bin/node
class Rectangle {
    constructor (width, height) {
      if (width > 0 && height > 0) {
        this.width = width;
        this.height = height;
      }
    }
  
    print (c = 'X') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  
    rotate () {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  
    double () {
      this.width *= 2;
      this.height *= 2;
    }
  }
  
  module.exports = Rectangle;