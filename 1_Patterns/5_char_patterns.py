n = int(input("Enter the number of rows: "))

"""
E 
D E 
C D E 
B C D E 
A B C D E 
"""
for i in range(n):
    for j in range(i+1):
        print(chr(64+n-i+j), end=' ')
    print()


print()
"""
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 
"""
for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for k in range(i+1):
        print(chr(65 + k), end=' ')
    for l in range(i, 0, -1):
        print(chr(64+l), end=' ')
    print()


print()
"""
A B C D E 
A B C D 
A B C 
A B 
A 
"""

for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end=' ')
    print()


print()
"""
A 
A B 
A B C 
A B C D 
A B C D E 
"""
for i in range(n):
    for j in range(i+1):
        print( chr(65 + j), end=' ')
    print()


print()
"""
A 
B B 
C C C 
D D D D 
E E E E E 
"""
for i in range(n):
    for j in range(i+1):
        print( chr(65 + i), end=' ')
    print()