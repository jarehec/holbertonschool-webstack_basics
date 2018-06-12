#!/usr/bin/node
let i = 0;
for (let item of process.argv) {
  if (i === 2) {
    console.log(item);
    i = 0;
    break;
  }
  i++;
}
if (i !== 0) {
  console.log('No argument');
}
