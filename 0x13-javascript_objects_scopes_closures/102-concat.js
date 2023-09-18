#!/usr/bin/node

const fs = require('fs');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const arg3 = process.argv[4];

const fileAText = fs.readFileSync(arg1, 'utf-8');
const fileBText = fs.readFileSync(arg2, 'utf-8');

const newText = fileAText.concat(fileBText);

fs.appendFileSync(arg3, newText, 'utf-8');
