#!/usr/bin/node
// Task 11
function secLargest (myList) {
  let first, second;
  if (myList !== undefined && myList.length >= 2) {
    if (myList[0] > myList[1]) {
      first = myList[0];
      second = myList[1];
    } else {
      first = myList[1];
      second = myList[0];
    }
    for (let i = 2; i < myList.length; i++) {
      if (first < myList[i]) {
        second = first;
        first = myList[i];
      } else if (second < myList[i]) {
        second = myList[i];
      }
    }
    return second;
  } else {
    return 0;
  }
}

const myList = process.argv.slice(2).map(i => parseInt(i));
console.log(secLargest(myList));
