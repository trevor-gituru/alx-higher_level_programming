#!/usr/bin/node
// Task 3

const request = require('request');
const requestURL = 'https://swapi-api.alx-tools.com';
const requestURI = '/api/films/' + process.argv[2];
const fullURL = requestURL + requestURI;
request(fullURL, function (err, response) {
  if (err) {
    return console.log(err);
  }
  if (response) {
    console.log(JSON.parse(response.body).title);
  }
});
