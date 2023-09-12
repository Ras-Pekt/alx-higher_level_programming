#!/usr/bin/node

const newList = require('./100-data').list;

const map1 = newList.map((x, idx) => x * idx);
console.log(newList);
console.log(map1);
