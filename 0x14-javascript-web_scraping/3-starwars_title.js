#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the SWAPI
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    // Print the movie title
    console.log(movie.title);
  }
});
