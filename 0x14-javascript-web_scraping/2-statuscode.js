#!/usr/bin/node
// a script that display the status code of a GET request

const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
}
);
