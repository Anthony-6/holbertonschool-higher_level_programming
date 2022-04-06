#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
const dataFileA = fs.readFileSync(arg[2], 'utf8');
const dataFileB = fs.readFileSync(arg[3], 'utf8');
const content = dataFileA + dataFileB;
fs.writeFile(arg[4], content, err => {
  if (err) {
    console.error(err);
  }
});
