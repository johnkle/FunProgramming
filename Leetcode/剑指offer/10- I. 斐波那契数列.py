class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = int((dp[i-1]+dp[i-2])%(1e9+7))
        return dp[n]

    
    # def fib2(self, n):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     memo = [-1 for i in range(n)]
    #     if memo[n-1] == -1:
    #         memo[n-1] = (self.fib(n-1)+self.fib(n-2))%1000000007
    #     return memo[n-1]
if __name__ == "__main__":
    sl = Solution()
    print(sl.fib(12))