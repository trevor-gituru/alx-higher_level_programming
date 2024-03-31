#!/usr/bin/node

const size = parseInt(process.argv[2]);
let i, j;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    let row = '';
    for (j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
