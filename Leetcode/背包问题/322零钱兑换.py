#参考279完全平方数 377组合总和4
#https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] == amount+1:
            return -1
        return dp[amount]

#内外循环区别 coin内循环无序有重复，外循环有序无重复
class Solution2:
    def coinChange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1