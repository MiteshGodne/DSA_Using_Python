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
    uni_2.sort()                       # TC - O((m+n)log(m+n)) & SC - O(n + m) 
    print(uni_2)
    
def union_set(nums1: list[int], nums2:list[int]) -> None:
    union = set(nums1+nums2)
    union = sorted(union)
    print(union)
   
arr1 = [1,3,5,5] 
arr2 = [4,4,15,26,47]   
union_hashmap(arr1, arr2)
union_set(arr1, arr2)