class Solution:
    def countSubstrings(self, s: str) -> int:
        rows = len(s)
        cols = len(s)
        dp = [[False]*cols for _ in range(rows)]
        count = 0
        for i in range(rows-1,-1,-1):
            for j in range(i,cols):
                if s[i] == s[j]:
                    dp[i][j] = j-i<2 or dp[i+1][j-1]
                if dp[i][j]:
                    count += 1
        return count