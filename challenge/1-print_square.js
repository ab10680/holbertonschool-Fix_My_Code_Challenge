#!/usr/bin/node
// Correct implementation of printing a square

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.error('Missing size');
  process.exit(1);
}

for (let i = 0; i < size; i++) {
  console.log('#'.repeat(size));
}
