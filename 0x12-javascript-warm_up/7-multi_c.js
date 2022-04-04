#!/usr/bin/node
const arg = process.argv;
const isInt = parseInt(process.argv[2]);
let i = 0;
if (isNaN(isInt)) {
  console.log('Missing number of occurrences');
} else { 
  while (i < arg[2]) {
    console.log('C is fun');
    i++;
  }
}
