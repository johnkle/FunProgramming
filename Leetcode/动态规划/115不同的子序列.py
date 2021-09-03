class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        #dp[i][j]表示s[...i]的子序列中t[...j]出现的个数
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]