#参考322零钱兑换
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1]*(n+1)
        #注意基本条件
        dp[0] = 0
        for i in range(1,n+1):
            for j in range(1,math.floor(pow(i,0.5))+1):
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]