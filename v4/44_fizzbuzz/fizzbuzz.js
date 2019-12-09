// FizzBuzz in JavaScript
// Made By Paulo Elienay II

fz = ""
fizzbuzz = range => {
    for (let i = 1; i < range; i++) {
        fz = ""
        if (i % 3 == 0) fz += "Fizz"
        if (i % 5 == 0) fz += "Buzz"
        if (fz != "") console.log(i, fz)
    }
}

fizzbuzz(100)
