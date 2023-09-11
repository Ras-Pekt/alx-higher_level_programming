#!/usr/bin/node

const arg1 = process.argv[2];

if (parseInt(arg1)) {
  for (let i = 0; i < Math.floor(arg1); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
