import collections
#贪心
class Solution:
    def longestPalindrome(self, s):
        lookup = collections.Counter(s)
        res = 0
        for x in lookup:
            res += lookup[x]//2*2
            if lookup[x]%2 == 1 and res%2 == 0:
                res += 1
        return res

#dp
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        s = sorted(s)
        dp = [0]*(len(s)+1)
        dp[1] = 1
        for i in range(2,len(dp)):
            if s[i-1] == s[i-2]:
                dp[i] = dp[i-2]+2
            else:
                if dp[i-1]%2 == 1:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1]+1
        return dp[-1]