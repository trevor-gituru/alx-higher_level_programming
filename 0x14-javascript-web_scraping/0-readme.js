#!/usr/bin/node
// Task 0

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
