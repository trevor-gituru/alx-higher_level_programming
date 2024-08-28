#!/usr/bin/node
// Task 10
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

const result = factorial(parseInt(process.argv[2]));
console.log(result);
