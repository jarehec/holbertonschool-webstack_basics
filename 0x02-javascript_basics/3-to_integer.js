#!/usr/bin/node
let i = 0;
for (let item of process.argv) {
  if (i === 2) {
    item = parseInt(item, 10);
    if (isNaN(item)) {
      console.log('Not a number');
    } else {
      console.log('My number: ' + item);
    }
    break;
  }
  i++;
}
