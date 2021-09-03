#原地排序
def partition(nums, l, r):
    v = nums[l]
    j = l
    for i in range(l + 1, r + 1):
        if nums[i] < v:
            nums[i], nums[j + 1] = nums[j + 1], nums[i]
            j += 1
    nums[l], nums[j] = nums[j], nums[l]
    return j

def quickSort(nums,l,r):
    if l >= r:
        return
    p = partition(nums,l,r)
    quickSort(nums,l,p-1)
    quickSort(nums,p+1,r)


nums = [5,3,9,1,7,6,2]
#quickSort(nums,0,len(nums)-1)
partition(nums,0,len(nums)-1)
print(nums)
