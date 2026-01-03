num = int(input("Enter the num till which you want fibonacci series : "))

def fibonacci(n):
    if n <= 0:
        return
    print(0, end=' ')
    if n == 1:
        return
    print(1, end=" ")
    curr, nxt = 1, 1
    while nxt <= n:
        print(nxt, end=" ")
        prev = curr
        curr = nxt
        nxt = prev + curr
fibonacci(num)        # TC = O(n)