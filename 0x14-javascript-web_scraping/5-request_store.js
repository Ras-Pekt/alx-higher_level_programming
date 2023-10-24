#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

if (process.argv.length < 4) {
  process.exit(1);
}

const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filename, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
