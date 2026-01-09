seq = input("Enter a string : ")

n = len(seq)
def palindrome(strg, i):
    global n
    if i <= n/2:
        if strg[i] == strg[n-i-1]:
            return palindrome(seq, i+1)
        return False 
    else:
        return True 
print(palindrome(seq, 0))
        