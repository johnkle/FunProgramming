# ??
class Solution:
    def maxSlidingWindow(self, nums, k):
        left = 0
        right = 0
        small = float('inf')
        large = float('-inf')
        window = []
        res = []
        while right < len(nums):
            window.append(nums[right])
            while right-left+1 > k:
                window.pop(0)
                left += 1
            if right-left+1 == k:
                res.append(max(window))
            right += 1
        return res