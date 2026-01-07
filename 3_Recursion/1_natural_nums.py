num = int(input("Enter a number : "))

# ascending natural numbers
def natural_nums_asc(curr, n):
    print(curr, end=" ")
    if curr == n:
        return
    natural_nums_asc(curr+1 , n)
natural_nums_asc(1,num)

print()
# descending natural numbers using forward recursion
def natural_nums_desc(n):
    print(n, end=" ")
    if n == 1:
        return
    natural_nums_desc(n-1)
natural_nums_desc(num)

print()
# Back tracking
def natural_nums_desc_bt(curr, n):
    if curr > n:
        return
    natural_nums_desc_bt(curr+1 , n)
    print(curr, end=" ")

# sice print is used after call, then due to backtracking (tasks done after returning), desc series will be printed
natural_nums_desc_bt(1,num)
