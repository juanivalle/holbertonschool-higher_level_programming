#!/usr/bin/node

const arg = process.argv[2];
const arg2 = process.argv[3];

let i = 0;
while (i <= arg.length) {
  if (i === 0) {
    console.log(arg);
  } else {
    console.log(arg2);
  }
  if (i === 0) {
    console.log('is');
  }
  i++;
}
