class Solution(object):
    def integerBreak(self, n):
        dp = [0]*(n+1)
        for i in range(2,n+1):
            #从j处拆分
            for j in range(i):
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]

print(list(range(-1,-5,-1)))
print(list(range(-5,-1)))