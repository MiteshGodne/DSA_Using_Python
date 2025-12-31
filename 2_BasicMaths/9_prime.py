from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= int(sqrt(n)):
        if n % i == 0:
            return False
        i = i+1
    return True

num = int(input("Enter a number to check for prime : "))
print(is_prime(num))


def prime_factorization(n):
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1
    return factors
print(prime_factorization(num))