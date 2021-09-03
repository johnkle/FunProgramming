class Solution:
    def canJump(self, nums):
        rightmost = 0
        for i in range(len(nums)):
            if i <= rightmost:
                rightmost = max(rightmost,i+nums[i])
                if rightmost >= len(nums)-1:
                    return True
        return False