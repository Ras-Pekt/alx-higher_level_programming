#!/usr/bin/node

const newList = require('./100-data').list;

const map1 = newList.map((x) => x * newList.indexOf(x));
console.log(newList);
console.log(map1);
