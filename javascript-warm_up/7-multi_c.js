#!/usr/bin/node

const arg = process.argv[2];

const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  if (!isNaN(num)) {
    console.log('C is fun');
  }
}
