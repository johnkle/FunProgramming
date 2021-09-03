#0-1背包，继续练习
class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for s in strs:
            s0 = s.count('0')
            s1 = s.count('1')
            for i in range(m,s0-1,-1):
                for j in range(n,s1-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-s0][j-s1]+1)
        return dp[-1][-1]