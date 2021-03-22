#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const secondBiggest = process.argv.slice(2);
  secondBiggest.sort((a, b) => b - a);
  console.log(secondBiggest[1]);
}
