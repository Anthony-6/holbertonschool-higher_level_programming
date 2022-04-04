#!/usr/bin/node
const arg = process.argv;
if (arg.length < 4) {
  console.log(0);
} else {
    const array = [];
    let i = 2;
    while (i < arg.length) {
    array[i] = parseInt(arg[i]);
    i++;
    }
    array.sort();
    console.log(i);
}
