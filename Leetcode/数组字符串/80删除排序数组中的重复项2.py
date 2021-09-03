class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+2]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)