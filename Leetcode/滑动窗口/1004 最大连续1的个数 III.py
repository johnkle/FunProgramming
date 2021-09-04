#寻找最多k个0的最长子数组
class Solution:
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        window = 0
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                window += 1
            while window > k:
                if nums[left] == 0:
                    window -= 1
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res