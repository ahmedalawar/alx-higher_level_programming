#!/usr/bin/node
//  script that prints My number: <first argument converted in integer>

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
