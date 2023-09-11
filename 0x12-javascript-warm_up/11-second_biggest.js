#!/usr/bin/node

const cmdArray = process.argv.slice(2);
const argArray = [];

for (let i = 0; i < cmdArray.length; i++) {
  argArray.push(Number(cmdArray[i]));
}

const maxNum = Math.max(...argArray);
const start = argArray.indexOf(maxNum);
argArray.splice(start, 1);
console.log(Math.max(...argArray));
