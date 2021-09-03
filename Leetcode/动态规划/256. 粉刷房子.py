#参考931矩阵下降路径最小和
class Solution:
    def minCost(self, costs):
        rows = len(costs)
        cols = len(costs[0])
        dp = [[float('inf')]*cols for _ in range(rows)]
        dp[0] = costs[0]
        for i in range(1,rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j+1],dp[i-1][j+2])+costs[i][j]
                elif j == cols-1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j-2])+costs[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j+1])+costs[i][j]
        return min(dp[-1])