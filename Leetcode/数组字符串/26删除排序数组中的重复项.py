class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1

class Solution2(object):
    def removeDuplicates(self, nums):
        cur = 0
        while cur < len(nums)-1:
            if nums[cur]==nums[cur+1]:
                nums.pop(cur)
            else:
                cur+=1
        return len(nums)
            
