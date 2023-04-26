#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let print = '';
    for (let j = 0; j < process.argv[2]; j++) {
      print = print + 'X';
    }
    console.log(print);
  }
}
