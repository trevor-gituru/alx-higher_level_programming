#!/usr/bin/node
// Task 4

const request = require('request');
const requestURL = process.argv[2];
const charId = '18';
request(requestURL, function (err, response) {
  if (err && response.statusCode !== 200) {
    return console.log(err);
  }
  if (response) {
    const movies = JSON.parse(response.body).results;
    let count = 0;
    for (const movie of movies) {
      for (const character of movie.characters) {
        if (character.includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
