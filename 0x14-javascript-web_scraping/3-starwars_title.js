#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
}
);
