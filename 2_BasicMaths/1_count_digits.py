num = abs(int(input("Enter a number : ")))
n = num
# Brute Force Approach
count = 0
while num >=1:
    count = count+1
    num = num/10
print("Count of digits is ", count)

#  Optimized Approach - The logarithmic base 10 of a positive integers gives the number of digits in n.
#  We add 1 to the result to ensure that the count is correct even for numbers that are powers of 10.
from math import log10, floor
print("Number of digits are : ",(floor(log10(n))) + 1)

