#转化为0-1背包问题，元素不可重复使用，nums外循环，neg内循环
class Solution:
    def findTargetSumWays(self, nums, target):
        if (sum(nums)-target)%2 != 0:
            return 0
        if sum(nums) -target < 0:
            return 0
        neg = (sum(nums)-target)//2
        dp = [0]*(neg+1)
        dp[0] = 1
        for num in nums:
            for i in range(neg,num-1,-1):
                dp[i] += dp[i-num]
        return dp[-1]