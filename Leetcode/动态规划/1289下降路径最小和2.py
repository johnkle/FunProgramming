class Solution:
    def minFallingPathSum(self, arr):
        if not arr or not arr[0]:
            return 0
        row = len(arr)
        col = len(arr[0])
        dp = [[float('inf')]*col for _ in range(row)]
        dp[-1] = arr[-1]
        for i in range(row-2,-1,-1):
            for j in range(col):
                for p in range(col):
                    #列下标不同时，更新路径
                    if p != j:
                        #注意arr[i][j]放在括号里
                        dp[i][j] = min(dp[i][j],dp[i+1][p]+arr[i][j])
        return min(dp[0])