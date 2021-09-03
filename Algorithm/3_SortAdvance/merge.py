count = []
def merge(nums1, nums2):
    if not nums1 or not nums2:
        return
    res = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            count.append(j)
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if i == len(nums1):
        res.extend(nums2[j:])
    if j == len(nums2):
        res.extend(nums1[i:])
        for k in range(i,len(nums1)):
            count.append(j)
    return count

nums1 = [2,4,6]
nums2 = [1,3,5]
print(merge(nums1,nums2))