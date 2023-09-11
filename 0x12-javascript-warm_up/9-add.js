#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  if (typeof a === 'undefined' || typeof b === 'undefined') {
    return (NaN);
  } else {
    return (Number(a) + Number(b));
  }
}

console.log(add(arg1, arg2));
