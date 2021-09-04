#不包含0的最长连续子数组
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        window = 0
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                window += 1
            while window > 0:
                if nums[left] == 0:
                    window -= 1
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        dp = [0]*(len(nums)+1)
        for i in range(1,len(dp)):
            if nums[i-1] == 1:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 0
        return max(dp)
