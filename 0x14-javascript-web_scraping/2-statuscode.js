#!/usr/bin/node
// Task 2

const request = require('request');
const requestURL = process.argv[2];
request(requestURL, function (err, response) {
  if (err) {
    return console.log(err);
  }
  if (response) {
    console.log('code:', response.statusCode);
  }
});
