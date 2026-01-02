in_list = eval(input("Enter the list elements separated by , in [] : "))
# Recursion
def rev_list(l, idx):
    global rev
    if idx < 0:
        return
    rev.append(l[idx])
    rev_list(l, idx-1)
rev = []
rev_list(in_list, len(in_list)-1)
print(rev)

# Slicing returns the reverse list but does not modify list itself
res = in_list[::-1]
print(res)

# Recursion with lesser iterations but modifies the original list
def rev_list_two_ptr(l, strt, end):
    if strt >= end:
        return
    in_list[strt], in_list[end] = in_list[end], in_list[strt]
    rev_list_two_ptr(l,strt+1, end-1)
rev_list_two_ptr(in_list,0, len(in_list)-1)
print(rev)
