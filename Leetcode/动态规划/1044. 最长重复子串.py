#超时
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        dp = [['']*(n+1) for _ in range(n+1)]
        res = ''
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+s[i-1]
                    res = max(res,dp[i][j],key=len)
        return res