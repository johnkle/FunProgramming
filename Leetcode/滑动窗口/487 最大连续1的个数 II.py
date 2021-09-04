class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        window = 0
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                window += 1
            while window > 1:
                if nums[left] == 0:
                    window -= 1
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        window = dict()
        res = 0
        while right < len(nums):
            c = nums[right]
            if c not in window:
                window[c] = 0
            window[c] += 1
            while window.get(0,0) > 1:
                window[nums[left]] -= 1
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res