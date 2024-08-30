#!/usr/bin/node
// Task 10
function converter (base) {
  return function (num) {
    return num.toString(base);
  };
}

exports.converter = converter;
