// Reads a number from standard input, doubles it, and writes to standard output

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a number: ', (input) => {
  const num = Number(input);
  if (isNaN(num)) {
    console.log('Invalid number');
  } else {
    console.log(num * 2);
  }
  rl.close();
});
