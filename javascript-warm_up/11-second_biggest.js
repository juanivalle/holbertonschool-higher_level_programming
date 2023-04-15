#!/usr/bin/node

const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);

if ((args.length < 2)) {
  console.log(0);
} else {
  for (let i = 1; i < args.length; i++) {
    if (args[i] < args[0]) {
      console.log(args[i]);
      break;
    }
  }
}
