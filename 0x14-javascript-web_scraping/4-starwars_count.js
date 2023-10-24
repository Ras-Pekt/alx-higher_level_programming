#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;

    for (const result of results) {
      for (const character of result.characters) {
        if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
