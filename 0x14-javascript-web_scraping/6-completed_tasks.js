#!/usr/bin/node
// Task 6

const request = require('request');
const requestURL = process.argv[2];
request(requestURL, function (err, response) {
  if (err && response.statusCode !== 200) {
    return console.log(err);
  }
  const tasks = JSON.parse(response.body);
  const finished = {};
  for (const task of tasks) {
    if (task.completed) {
      if (task.userId in finished) {
        finished[task.userId]++;
      } else {
        finished[task.userId] = 1;
      }
    }
  }
  console.log(finished);
});
