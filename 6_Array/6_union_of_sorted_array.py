from collections import Counter

def union_hashmap(nums1: list[int], nums2:list[int]) -> None:
    freq = {}
    uni_1 = []
    for i in range(len(nums1)):
        freq[nums1[i]] = freq.get(nums1[i], 0) + 1
    for i in range(len(nums2)):
        freq[nums2[i]] = freq.get(nums2[i], 0) + 1
    for i in freq:
        uni_1.append(i)
    uni_1.sort()                       # TC - O((m+n)log(m+n)) & SC - O(n + m) 
    print(uni_1)     
       
    # OR 
    num_dict = Counter(nums1 + nums2)
    uni_2 = []
    for i in num_dict.items():
        uni_2.append(i[0])
    uni_2.sort()                       
    print(uni_2)
    
def union_set(nums1: list[int], nums2:list[int]) -> None:
    union = set(nums1+nums2)
    union = sorted(union)
    print(union)
    
from sortedcontainers import SortedSet
def union_sorted_set(nums1: list[int], nums2:list[int]) -> None:
    union = SortedSet(nums1+nums2)           
    print(union)
    
def union(nums1: list[int], nums2:list[int]) -> None:
    i = j = 0
    n = len(nums1)
    m = len(nums2)
    res = []
    if n<=0 or m<=0:                                    # Atleast 1 element required
        return                                  
    if nums1[i] < nums2[j]:
        res.append(nums1[i])
        i+=1 
    else:
        res.append(nums2[j])
        j+=1    
    while (i<n or j<m):
        if i<n and nums1[i] == res[-1]:
            i+=1
        elif j<m and nums2[j] == res[-1]:
            j+=1
        else:
            if i<n and j<m:
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i+=1
                    -1+=1
                else:
                    res.append(nums2[j])
                    j+=1
                    -1+=1
            elif i<n and nums1[i] != res[-1]:
                res.append(nums1[i])
                i+=1
                -1+=1
            else:
                res.append(nums2[j])
                j+=1
                -1+=1              
    return res
   
arr1 = [1,1,2,2] 
arr2 = [3,4,5]   
union_hashmap(arr1, arr2)
union_set(arr1, arr2)
union_sorted_set(arr1, arr2)
print(union(arr1, arr2))