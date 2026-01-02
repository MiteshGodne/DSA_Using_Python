from math import pow
num = int(input("Enter a number : "))

def count_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = int(n/10)
    return count

def armstrong(n):
    count = count_digits(n)
    copy = n
    result = 0
    while copy > 0:
        last_digit = copy % 10
        result = result + pow(last_digit, count)
        copy = int(copy/10)
    if result == n:
        print("Armstrong number.")
    else:
        print("Not an armstrong number.")
armstrong(num)