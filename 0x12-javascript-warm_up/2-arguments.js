#!/usr/bin/node
const arg = process.argv;
if (arg.length < 3) {
  console.log('No argument');
} if (arg.length === 3) {
  console.log('Argument found');
}
if (arg.length > 3) {
  console.log('Arguments found');
}
