#参考72编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m*n == 0:
            return m+n
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                left = dp[i][j-1]+1
                up = dp[i-1][j]+1
                leftup = dp[i-1][j-1]+2
                if word1[i-1] == word2[j-1]:
                    leftup -= 2
                dp[i][j] = min(left,up,leftup)
        return dp[m][n]

#参考1143最长公共子序列
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        if m*n == 0:
            return m+n
        def lcs(word1,word2):
            dp = [[0]*(n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            return dp[m][n]
        return m+n-2*lcs(word1,word2)