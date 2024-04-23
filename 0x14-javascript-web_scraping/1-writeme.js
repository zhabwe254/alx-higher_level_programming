#!/usr/bin/node

const fs = require('fs');

const file = process.argv[3];
const message = process.argv[4];

try {
  fs.writeFileSync(file, message, 'utf8');
  console.log(`"${message}" written to file ${file}`);
} catch (err) {
  console.error(err);
}
