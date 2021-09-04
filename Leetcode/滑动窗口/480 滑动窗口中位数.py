# ??
class Solution:
    def medianSlidingWindow(self, nums, k):
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
                window.sort()
                res.append(int(window[1]))
            right += 1
        return res