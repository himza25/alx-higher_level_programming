#!/usr/bin/node
const fs = require('fs');

const [,, fileA, fileB, fileC] = process.argv;

const contentA = fs.readFileSync(fileA, { encoding: 'utf-8' });
const contentB = fs.readFileSync(fileB, { encoding: 'utf-8' });

fs.writeFileSync(fileC, contentA + contentB);
