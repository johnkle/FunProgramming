class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n > 0:
            dp = [x for _ in range(n)]
            for i in range(1,n):
                dp[i] = dp[i-1]*x
            return dp[n-1]
        if n < 0:
            dp = [1/x for _ in range(-n)]
            for i in range(1,-n):
                dp[i] = 1/x*dp[i-1]
            return dp[-n-1]

class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x,-n)
        return self.myPow(x,n//2) if n%2==0 else x*self.myPow(x,n//2)


if __name__ == "__main__":
    sl = Solution()
    print(sl.myPow(2,-3))