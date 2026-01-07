num = int(input("Enter a number : "))
# ascending natural numbers
def natural_nums_asc(curr, n):
    print(curr, end=" ")
    curr += 1
    if curr > num:
        return
    natural_nums_asc(curr,n)
natural_nums_asc(1,num)

print()
# descending natural numbers
def natural_nums_desc(n):
    print(n, end=" ")
    if n == 1:
        return
    natural_nums_desc(n-1)
natural_nums_desc(num)