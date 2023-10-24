#!/usr/bin/node
// a script that reads and prints the content of a file

const fs = require('fs');

if (process.argv.length < 3) {
  process.exit(1);
}

const arg = process.argv[2];
fs.readFile(arg, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
}
);
