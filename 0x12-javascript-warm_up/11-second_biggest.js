#!/usr/bin/node
const arg = process.argv;
if (arg.length < 4) {
  console.log(0);
} else {
  const arr = [];
  let i = 2;
  while (i < arg.length) {
    arr[i - 2] = parseInt(arg[i]);
    i++;
  }
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  const second = Math.max.apply(null, arr);
  console.log(second);
}
