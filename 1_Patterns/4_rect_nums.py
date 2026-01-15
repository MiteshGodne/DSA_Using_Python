n = int(input("Enter the number of rows : "))

"""
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
"""
dec = n+1
for i in range(n):
    dec -= 1
    for j in range(n, n-i-1, -1):
        print(j, end=' ')
    for k in range(n, 2*i-2, -1):
        print(dec, end=' ')
    for l in range(n-i+1, n+1):
        print(l, end=' ')
    print()

for i in range(n-1):
    dec += 1
    for j in range(n, i+1, -1):
        print(j, end=' ')
    for k in range(2*i+1):
        print(dec, end=' ')
    for l in range(dec, n+1):
        print(l, end=' ')
    print()

print()
"""
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 
"""
for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    for k in range(2*(n-i)-2):
        print(' ', end=' ')
    for l in range(i+1, 0, -1):
        print(l, end=' ')
    print()
