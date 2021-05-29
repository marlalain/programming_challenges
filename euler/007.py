# By listing the first six prime numbers: 2, 3, 5, 7, 11,
# and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def find_next_prime(number):
    while True:
        number = number + 1
        if is_prime(number):
            return number


def main():
    answer = 0
    primes = []
    while len(primes) != 10001:
        answer = find_next_prime(answer)
        print("Testing " + str(len(primes)) + "/10001")
        primes.append(answer)
    print(answer)


if __name__ == "__main__":
    main()
