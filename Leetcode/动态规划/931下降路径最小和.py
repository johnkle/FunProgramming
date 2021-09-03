#我们用 dp[i,j]表示从位置为 (i,j) 的元素开始的下降路径最小和
class Solution:
    def minFallingPathSum(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        dp[-1] = matrix[-1]
        for i in range(row-2,-1,-1):
            for j in range(col):
                if j == 0:
                    dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+matrix[i][j]
                elif j == col-1:
                    dp[i][j] = min(dp[i+1][j],dp[i+1][j-1])+matrix[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])+matrix[i][j]
        return min(dp[0])

#dp[i,j]表示从第一行下降到 (i,j) 的下降路径最小和
class Solution:
    def minFallingPathSum(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        dp[0] = matrix[0]
        for i in range(1,rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
                elif j == cols-1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+matrix[i][j]
        return min(dp[-1])