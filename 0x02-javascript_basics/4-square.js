#!/usr/bin/node
let i = parseInt(process.argv[2], 10);
if (isNaN(i)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < i; x++) {
    console.log('X'.repeat(i));
  }
}
