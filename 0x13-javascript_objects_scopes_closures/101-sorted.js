#!/usr/bin/node

const newDict = require('./101-data').dict;

const idByOccurence = {};

for (const uid in newDict) {
  const occurence = newDict[uid];

  if (idByOccurence[occurence] === undefined) {
    idByOccurence[occurence] = [];
  }

  idByOccurence[occurence].push(uid);
}

console.log(idByOccurence);
