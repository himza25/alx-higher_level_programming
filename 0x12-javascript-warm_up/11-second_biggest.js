#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
let max = -Infinity;
let secondMax = -Infinity;

for (const num of args) {
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num !== max) {
    secondMax = num;
  }
}

console.log(args.length <= 1 ? 0 : secondMax);
