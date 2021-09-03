class Solution:
    def numWays(self, n, k):
        if n == 1:
            return k
        if n == 2:
            return pow(k,2)
        #dp[i][0/1] 用k种颜色涂i个栅栏的涂法数,0第i个栅栏与前一个栅栏颜色相同，1不同
        dp = [[0,0] for _ in range(n)]
        dp[0] = [0,k]
        for i in range(1,n):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = (dp[i-1][0]+dp[i-1][1])*(k-1)
        return sum(dp[-1])