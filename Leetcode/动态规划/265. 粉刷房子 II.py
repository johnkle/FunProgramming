#参考下降路径最小和1289
class Solution:
    def minCostII(self, costs):
        rows = len(costs)
        cols = len(costs[0])
        dp = [[float('inf')]*cols for _ in range(rows)]
        dp[0] = costs[0]
        for i in range(1,rows):
            for j in range(cols):
                for k in range(cols):
                    if j != k:
                        dp[i][j] = min(dp[i][j],dp[i-1][k]+costs[i][j])
        return min(dp[-1])