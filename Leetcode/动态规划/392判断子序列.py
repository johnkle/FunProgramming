class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        m = len(s)
        n = len(t)
        dp = [[False]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = True
        for i in range(1,m+1):
            for j in range(i,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m][n]

#参考1143最长公共子序列
class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(i,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[m][n] == len(s)