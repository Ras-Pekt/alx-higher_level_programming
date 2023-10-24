#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const request = require('request');

if (process.argv.length < 2) {
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const taskDict = {};

    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (taskDict[task.userId] === undefined) {
          taskDict[task.userId] = 0;
        }
        taskDict[task.userId]++;
      }
    }
    console.log(taskDict);
  }
});
