class Solution(object):
    def exchange(self, nums):
        l = 0
        r = len(nums)-1
        while l < r:
            while l<r and nums[l]%2 != 0:
                l += 1
            while l<r and nums[r]%2 == 0:
                r -= 1
            nums[l],nums[r] = nums[r],nums[l]
        return nums