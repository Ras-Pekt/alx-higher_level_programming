#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

const request = require('request');

if (process.argv.length < 2) {
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function getCharacter (characterURL) {
  request(characterURL, (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    for (const character of JSON.parse(body).characters) {
      getCharacter(character);
    }
  }
});
