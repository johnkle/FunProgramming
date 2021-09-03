class Solution(object):
    def wordBreak(self, s, wordDict):
        #dp[i]表示前i个字符组成的字符串s[0...i-1]是否能正确拆分
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(dp)):
            for j in range(i):
               if dp[j] and (s[j:i] in wordDict):
                   dp[i] = True
                   break
        return dp[len(s)]

class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for j in range(i):
                if s[j:i] in wordDict:
                    dp[i] |= dp[j]
        return dp[-1]