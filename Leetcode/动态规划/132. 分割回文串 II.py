class Solution:
    def minCut(self, s):
        #先check回文子串
        def check(s):
            matrix = [[False]*len(s) for _ in range(len(s))]
            for i in range(len(matrix)-1,-1,-1):
                for j in range(i,len(matrix)):
                    if s[j] == s[i]:
                        matrix[i][j] = j-i<2 or matrix[i+1][j-1]
            return matrix
        matrix = check(s)
        #背包问题
        dp = [float('inf')]*len(s)
        dp[0] = 0
        for i in range(1,len(dp)):
            if matrix[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if matrix[j+1][i]:
                        dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]