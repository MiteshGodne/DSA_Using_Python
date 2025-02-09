def is_palindrome_num(n):
    reverse = 0
    while n > 0:
        last_digit = n%10
        reverse =  reverse * 10 + last_digit
        n = int(n / 10)
    if num == reverse:
        return True
    else:
        return False

num = int(input("Enter a number : "))
print(is_palindrome_num(num))          #  Time Complexity = O(log_10 n) where n is number of digits in num
