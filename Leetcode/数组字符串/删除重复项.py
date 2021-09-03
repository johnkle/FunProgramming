def removeDuplicates(self, nums):
    if not nums:
        return
    temp = 0
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            temp = nums[i]
        if nums[i] == temp:
            nums.pop(i)
