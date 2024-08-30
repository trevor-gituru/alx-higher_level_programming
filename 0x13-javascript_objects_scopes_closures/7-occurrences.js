#!/usr/bin/node
// Task 7

exports.nbOccurences = (list, element) => {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === element) {
      count++;
    }
  }
  return count;
};
