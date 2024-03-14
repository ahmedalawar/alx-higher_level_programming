#!/usr/bin/node
//  script that prints x times “C is fun”

let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (i < Number(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
