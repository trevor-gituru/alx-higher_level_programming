#!/usr/bin/node
// Task 5

const request = require('request');
const fs = require('fs');
const requestURL = process.argv[2];
const file = process.argv[3];
request(requestURL, function (err, response) {
  if (err && response.statusCode !== 200) {
    return console.log(err);
  }
  fs.writeFile(file, response.body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
