#!/usr/bin/node
const arg = process.argv;
const isInt = parseInt(arg[2]);
if (isNaN(isInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg[2]; i++) {
    console.log('X'.repeat(arg[2]));
  }
}
