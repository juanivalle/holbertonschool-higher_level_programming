#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const arg = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg) || isNaN(arg2)) {
  console.log('NaN');
} else {
  console.log(add(arg, arg2));
}
