#!/usr/bin/node
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
