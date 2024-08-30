#!/usr/bin/node
// Task 9
function logMe () {
  let count = 0;
  function print (text) {
    console.log(`${count}: ${text}`);
    count++;
  }
  return print;
}
exports.logMe = logMe();
