#!/usr/bin/node

const argu = process.argv - 2;
if (argu === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
