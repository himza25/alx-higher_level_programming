#!/usr/bin/node

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // If an error occurred, print the error object
    console.error(err);
  } else {
    // If no error, print the file content
    console.log(data);
  }
});
