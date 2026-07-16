num = int(input("Enter a number : "))
exp = int(input("Enter the power : "))

def power(a, pw):
    res = 1                 # stores multiple to make power even
    while pw > 0:
        if pw % 2 != 0:       # if power is odd, make it even : a^odd -> a*a^even
            res *= a
        pw //= 2       # half the power
        a = a * a      # square the base
    return res

print(power(num, exp))   # TC = O(log_2(n)) as everytime power is divided by 2 so loop doesn't run n times
