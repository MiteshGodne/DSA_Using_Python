from math import sqrt, ceil
def divisors(n):
    l = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
            if i != n/i:    # used to prevent it from including perfect sqrt number twice
                l.append(int(n/i))
    return l
num = int(input("Enter a number : "))
print(divisors(num))               # Time Complexity - O(sqrt(n))


def sorted_divisors(n):
    l = []
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            l.append(i)
    for i in range(int(sqrt(n)), 0, -1):
        if n % i == 0:
            l.append(int(n/i))
    return l
print(sorted_divisors(num))          # Time Complexity - O(sqrt(n))
