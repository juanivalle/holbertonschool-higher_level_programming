#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || (n <= 1)) {
    return 1;
  } else {
    let result = 1;
    for (let i = 1; i <= n; i++) {
      result *= i;
    }
    return result;
  }
}
const arg1 = parseInt(process.argv[2]);
console.log(factorial(arg1));
