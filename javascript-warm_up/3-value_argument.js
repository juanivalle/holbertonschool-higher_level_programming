#!/usr/bin/node

const [argv] = process.argv.slice(2);
if (argv) {
  console.log(argv);
} else {
  console.log('No argument');
}
