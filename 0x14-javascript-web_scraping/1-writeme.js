#!/usr/bin/node
// Task 1

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, function (err) {
  if (err) {
    console.error(err);
  }
});
