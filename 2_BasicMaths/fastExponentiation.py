num = int(input("Enter a number : "))
exp = int(input("Enter the power : "))


def power(n, pw):
    res = 1                 # stores multiple to make power even
    while pw > 0:
        if pw % 2 != 0:
            res *= n
        pw = int(pw / 2)    # half the power
        n = n * n      # square the base
    return res

print(power(num, exp))                  # TC = O(log_2 (n)) as everytime power is divided by 2 so loop doesn't run n times
