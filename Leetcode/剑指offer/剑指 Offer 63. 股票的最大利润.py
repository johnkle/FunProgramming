#dp[i]表示以prices[i]结尾的前i日的最大利润
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [0]*len(prices)
        for i in range(1,len(dp)):
            dp[i] = max(dp[i-1],prices[i]-min(prices[:i]))
        return dp[len(prices)-1]

#dp[i] 第i天卖出股票的最大利润=第i天的价格-前i天的最小值
class Solution2:
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [0 for _ in range(len(prices))]
        minprice = prices[0]
        res = 0
        for i in range(1,len(dp)):
            minprice = min(minprice,prices[i])
            dp[i] = prices[i]-minprice
        return max(dp)

class Solution3:
    def maxProfit(self, prices):
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(dp)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]