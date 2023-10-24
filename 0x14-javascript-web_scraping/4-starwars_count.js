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
    try {
      const jsonBody = JSON.parse(body);
      const results = jsonBody.results;
      let count = 0;

      for (const result of results) {
        const characters = result.characters;
  
        for (const character of characters) {
          if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
            count++;
          }
        }
      }
      console.log(count);
    } catch (error) {
      console.log(error);
    }
  }
}
);
