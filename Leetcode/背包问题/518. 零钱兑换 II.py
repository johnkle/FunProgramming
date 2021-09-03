class Solution:
    def change(self, amount, coins):
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(1,amount+1):
                if i < coin:
                    continue
                dp[i] += dp[i-coin]
        return dp[-1]