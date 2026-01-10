num = int(input("Enter a number : "))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(num):
    print(fibonacci(i), end=" ")  

# Exponential TC nearly equal to  O(2^n)  