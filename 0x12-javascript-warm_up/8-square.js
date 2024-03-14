#!/usr/bin/node
//  script that prints a square

let j = 0;

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  while (j < Number(process.argv[2])) {
    console.log('X'.repeat(Number(process.argv[2])));
    j++;
  }
}
