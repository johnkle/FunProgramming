class Solution(object):
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        #不能用[[0]*(n+1)]*(m+1)，这样是同一个引用
        dp = [[0]*(n+1) for _ in range(m+1)]
        side = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    side = max(side,dp[i][j])
        return side*side

class Solution2:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]
        side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                    side = max(side,dp[i][j])
        return side*side