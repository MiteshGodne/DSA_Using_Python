num1 = abs(int(input("Enter a number : ")))
num2 = abs(int(input("Enter another number : ")))

#
def gcd_by_euclid_recursion(n1, n2):
    small = min(n1, n2)
    large = max(n1, n2)
    if small == 0:
        return large
    else:
        return gcd_by_euclid_recursion(large-small, small)
print("GCD : ", gcd_by_euclid_recursion(num1, num2))           ## TC = O(n)

def gcd_by_euclid(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 >= n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    if n1 == 0:
        return n2
    else:
        return n1
print("GCD : ", gcd_by_euclid(num1, num2))           ## TC = O(n)

## Optimized by Gabriel Lame
def gcd_by_gabriel(n1, n2):
    mini, maxi = min(n1,n2), max(n1,n2)
    if mini == 0:
        return maxi
    else:
        return gcd_by_gabriel(maxi % mini, mini)

print("GCD : ", gcd_by_gabriel(num1, num2))           # TC = O(log_phi min(num1, num2))