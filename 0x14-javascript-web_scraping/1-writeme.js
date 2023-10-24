#!/usr/bin/node
// a script that writes a string to a file

const fs = require('fs');

if (process.argv.length < 4) {
  process.exit(1);
}

const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, (err) => {
  if (err) {
    console.error(err);
  }
}
);
