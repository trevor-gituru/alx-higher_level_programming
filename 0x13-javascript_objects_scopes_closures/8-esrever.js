#!/usr/bin/node
exports.esrever = (list) => {
  const revList = [];
  for (let i = (list.length - 1), j = 0; i >= 0; i--, j++) {
    revList[j] = list[i];
  }
  return revList;
};
