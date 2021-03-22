#!/usr/bin/node
const firstargument = process.argv;
if (firstargument[2] === undefined) {
  console.log('No argument');
} else {
  console.log(firstargument[2]);
}
