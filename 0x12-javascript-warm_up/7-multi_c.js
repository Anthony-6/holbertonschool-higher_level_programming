#!/usr/bin/node
const arg = process.argv;
const isInt = parseInt(arg[2]);
if (isNaN(isInt)) {
  console.log('Missing number of occurences');
} else { 
  for (i = 0; i < arg[2]; i++) {
    console.log('C is fun');
  }
}
