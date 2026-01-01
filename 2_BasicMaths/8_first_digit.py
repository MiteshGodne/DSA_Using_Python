from math import pow, log10
num = int(input("Enter a number : "))

ten_raised_to = int(log10(num))
first_digit = int(num / pow(10, ten_raised_to))

print(first_digit)