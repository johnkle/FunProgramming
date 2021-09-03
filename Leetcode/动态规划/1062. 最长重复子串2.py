class Solution:
    def longestRepeatingSubstring(self, s):
        n = len(s)
        res = 0
        #dp[i][j] s[...i]和s[...j]的重复子串的长度
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                res = max(res,dp[i][j])
        return res