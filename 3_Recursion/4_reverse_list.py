in_list = eval(input("Enter the list elements separated by , in [] : "))
# # Recursion
# def rev_list(l, idx):
#     global rev
#     if idx < 0:
#         return
#     rev.append(l[idx])
#     rev_list(l, idx-1)
# rev = []
# rev_list(in_list, len(in_list)-1)
# print(rev)

# # Slicing returns the reverse list but does not modify list itself
# res = in_list[::-1]
# print(res)

# Recursion with lesser iterations but modifies the original list
def rev_list_two_ptr(lst, i, n):
    if i >= n/2:
        return
    lst[i], lst[n-i-1] = lst[n-i-1], lst[i]
    rev_list_two_ptr(lst, i+1, n)
rev_list_two_ptr(in_list, 0, len(in_list))
print(in_list)
