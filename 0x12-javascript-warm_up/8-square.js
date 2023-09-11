#!/usr/bin/node

const arg1 = process.argv[2];

if (parseInt(arg1)) {
  for (let i = 0; i < Math.floor(arg1); i++) {
    let row = '';
    for (let j = 0; j < Math.floor(arg1); j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
