#!/usr/bin/node

const arg = process.argv[2];

const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  let value = '';
  for (let j = 0; j < num; j++) {
    value += 'X';
  }
  if (!isNaN(num)) {
    console.log(value);
  }
}
