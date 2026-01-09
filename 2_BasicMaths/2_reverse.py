num = int(input("Enter a number : ").rstrip('0'))   # removing trailing zeroes
res = 0
while int(num) > 0:
    rem = int(num) % 10
    num /= 10
    res = res*10 + rem
print("Reverse of the number is : ",res)

#  Time Complexity = O(log_10 n) where n is number of digits in num