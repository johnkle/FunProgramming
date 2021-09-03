class Solution:
    def maxProduct(self, nums):
        dp = [[0,0] for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        res = nums[0]
        for i in range(1,len(dp)):
            if nums[i] > 0:
                dp[i][0] = max(dp[i-1][0]*nums[i],nums[i])
                dp[i][1] = min(dp[i-1][1]*nums[i],nums[i])
            elif nums[i] < 0:
                dp[i][0] = max(dp[i-1][1]*nums[i],nums[i])
                dp[i][1] = min(dp[i-1][0]*nums[i],nums[i])
            res = max(res,dp[i][0])
        return res

class Solution2:
    def maxProduct(self, nums):
        dp = [[0]*len(nums) for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>0:
                dp[0][i] = max(dp[0][i-1]*nums[i],nums[i])
                dp[1][i] = min(dp[1][i-1]*nums[i],nums[i])
            elif nums[i]<0:
                dp[0][i] = max(dp[1][i-1]*nums[i],nums[i])
                dp[1][i] = min(dp[0][i-1]*nums[i],nums[i])
        for i in range(len(nums)):
            res = max(res,dp[0][i])
        return res



