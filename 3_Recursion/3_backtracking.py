# Back tracking
num = int(input("Enter a number : "))

def natural_nums_desc_bt(curr, n):
    if curr > n:
        return
    natural_nums_desc_bt(curr+1 , n)
    print(curr, end=" ")
# sice print is used after call, then due to backtracking (tasks done after returning), desc series will be printed
natural_nums_desc_bt(1,num)


print()
def natural_nums_asc_bt(n):
    if n == 0:
        return
    natural_nums_asc_bt(n-1)
    print(n, end=" ")
natural_nums_asc_bt(num)
