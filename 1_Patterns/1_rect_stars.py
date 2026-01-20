n = int(input("Enter the number of rows: "))


"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
"""
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or j ==0 or j ==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()



print()
"""
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
"""
for i in range(n):
    for o in range(i+1):
        print('*', end=' ')
    for p in range(2*(n-i)-2):
        print(' ', end=' ')
    for q in range(i+1):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(n-i, 0, -1):
        print('*', end=' ')
    for k in range(2*i):
        print(' ', end=' ')
    for l in range(n-i, 0, -1):
        print('*', end=' ')
    print()



print()
"""
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
"""
for i in range(n):
    for j in range(n-i, 0, -1):
        print('*', end=' ')
    for k in range(2*i):
        print(' ', end=' ')
    for l in range(n-i, 0, -1):
        print('*', end=' ')
    print()
for i in range(n):
    for o in range(i+1):
        print('*', end=' ')
    for p in range(2*(n-i)-2):
        print(' ', end=' ')
    for q in range(i+1):
        print('*', end=' ')
    print()





print()
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

