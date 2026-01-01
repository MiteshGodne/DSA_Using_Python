from math import sqrt
num = int(input("Enter a number : "))

def trailing_zeroes_in_factorial(n):
    i = 5
    res = 0
    while i <= n:
        res = res + (n/i)
        i = i*i
    return int(res)
print(trailing_zeroes_in_factorial(num))               # Time complexity -> O(log2(log5(n))