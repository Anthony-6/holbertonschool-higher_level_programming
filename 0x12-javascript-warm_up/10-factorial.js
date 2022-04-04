#!/usr/bin/node
function factorial (i) {
  const isInt = parseInt(i);
  if (isNaN(isInt) || i === 0) {
    return 1;
  } else {
    return i * factorial(isInt - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
