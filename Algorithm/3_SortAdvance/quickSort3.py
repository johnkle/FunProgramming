def partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

def quickSort(nums,l,r):
    if l >= r:
        return
    p = partition(nums,l,r)
    quickSort(nums,l,p-1)
    quickSort(nums,p+1,r)

nums = [5,3,9,1,7,6,2]
print(quickSort(nums,0,len(nums)-1))
print(partition(nums,0,len(nums)-1))
print(nums)