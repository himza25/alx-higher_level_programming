#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesId = '18';
  let count = 0;

  films.forEach(film => {
    if (film.characters.some(characterUrl => characterUrl.includes(wedgeAntillesId))) {
      count++;
    }
  });

  // Print the count of films featuring Wedge Antilles
  console.log(count);
});
