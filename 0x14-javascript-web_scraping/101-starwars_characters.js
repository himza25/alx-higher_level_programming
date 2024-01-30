#!/usr/bin/node

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);

// Get the movie ID from the command line arguments
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

const getCharacterName = async (characterUrl) => {
  try {
    const response = await requestPromise(characterUrl);
    const character = JSON.parse(response.body);
    console.log(character.name);
  } catch (error) {
    console.error(error);
  }
};

const printCharacters = async () => {
  try {
    const response = await requestPromise(url);
    const characters = JSON.parse(response.body).characters;
    for (const characterUrl of characters) {
      await getCharacterName(characterUrl);
    }
  } catch (error) {
    console.error(error);
  }
};

printCharacters();
