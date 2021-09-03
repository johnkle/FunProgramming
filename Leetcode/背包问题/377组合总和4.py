#参考322
#https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]