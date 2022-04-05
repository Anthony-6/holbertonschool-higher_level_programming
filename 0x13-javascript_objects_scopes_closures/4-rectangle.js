#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
    this.width = w;
    this.height = h;
    }
  }
  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
  rotate () {
    const saveheight = this.height;
    this.height = this.width;
    this.width = saveheight;
  }
};
