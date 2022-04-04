#!/usr/bin/node
function factorial (i) {
  const isInt = parseInt(i);
  if (isNaN(isInt) || i) {
    return 1;
  } else {
      return x * factorial(isInt - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
