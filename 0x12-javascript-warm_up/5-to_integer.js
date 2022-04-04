#!/usr/bin/node
const arg = process.argv;
const isInt = parseInt(arg[2]);
if (isNaN(isInt)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + isInt);
}
