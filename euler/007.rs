// By listing the first six prime numbers: 2, 3, 5, 7, 11,
// and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?

fn is_prime(number: i64) -> bool {
    if number <= 1 {
        return false;
    }
    for n in 2..number {
        if number % n == 0 {
            return false;
        }
    }
    return true;
}

fn find_next_prime(mut number: i64) -> i64 {
    loop {
        number += 1;
        if is_prime(number) {
            return number;
        }
    }
}

fn main() {
    let mut answer: i64 = 0;
    let mut primes = Vec::new();
    while primes.len() != 10001 {
        answer = find_next_prime(answer);
        print!("\rTesting {:?}/10001: {:?}", primes.len() + 1, answer);
        //println!("Testing {:?}/10001: {:?}", primes.len() + 1, answer);
        primes.push(answer);
    }

    println!("\nThe answer is: {:?}", answer);
}
