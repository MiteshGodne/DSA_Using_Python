n = int(input("Enter the number of rows: "))
"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end=' ')
        num += 1
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


"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""

for i in range(n):
    for j in range(i+1):
        if (i+j)%2==0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
for i in range(n):
    for j in range(i + 1):
        print(j+1, end=' ')
    print()

"""
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""
for i in range(n):
    for j in range(i + 1):
        print(i+1, end=' ')
    print()

"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
for i in range(n, 0, -1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()