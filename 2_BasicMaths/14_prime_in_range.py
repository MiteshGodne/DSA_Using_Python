def prime_in_range(n):
    # Making true all the indices for prime
    primes = [True for i in range(n+1)]

    counter = 2
    while counter < n+1:
        if primes[counter]:
            i = counter+counter
            while i <= n:
                primes[i] = False  # Changing multiples of all primes to False
                i = i+counter
        counter += 1
    for i in range(2,n+1):
        if primes[i]:
            print(i, end=" ")

num = int(input("Enter a no. till you want prime number : "))

prime_in_range(num)