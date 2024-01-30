#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Print the character name
      console.log(JSON.parse(body).name);
    });
  });
});
