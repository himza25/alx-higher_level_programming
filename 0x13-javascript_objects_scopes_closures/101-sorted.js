#!/usr/bin/node
const { dict } = require('./101-data');
const sorted = {};

for (const key in dict) {
  if (sorted[dict[key]]) {
    sorted[dict[key]].push(key);
  } else {
    sorted[dict[key]] = [key];
  }
}

console.log(sorted);
