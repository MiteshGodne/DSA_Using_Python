num = int(input("Enter a number : "))
temp = 1
# ascending natural numbers
def natural_nums_asc(n):
    global temp, num
    print(temp, end=" ")
    temp += 1
    if temp > num:
        return
    natural_nums_asc(n-1)
natural_nums_asc(num)

print()
# descending natural numbers
def natural_nums_desc(n):
    print(n, end=" ")
    if n == 1:
        return
    natural_nums_desc(n-1)
natural_nums_desc(num)