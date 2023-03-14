#!/usr/bin/node
function factorial(number) {
    if (number == 1) return 1
    else return factorial(number) * factorial(number - 1)
}

if (isNaN(process.argv[2])) {
    console.log(factorial(1))
} else {
    console.log(factorial(process.argv[2]))
}
