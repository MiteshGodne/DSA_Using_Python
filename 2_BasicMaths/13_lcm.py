num1 = abs(int(input("Enter a number : ")))
num2 = abs(int(input("Enter another number : ")))

def gcd_by_gabriel(n1, n2):
    mini, maxi = min(n1,n2), max(n1,n2)
    if mini == 0:
        return maxi
    else:
        return gcd_by_gabriel(maxi % mini, mini)

def lcm_by_gabriel(n1, n2):
    return int(n1*n2 / gcd_by_gabriel(n1, n2))

print(lcm_by_gabriel(num1, num2))