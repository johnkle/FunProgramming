# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 最终的答案即为所有 dp[i][j]==True 中 j−i+1（即子串长度）的最大值

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ''
        dp = [[True]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    dp[i][j] = j-i<2 or dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j-i+1 > len(res):
                    res = s[i:j+1]
        return res

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ''
        dp = [[True]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = False
                if dp[i][j] and j-i+1 > len(res):
                    res = s[i:j+1]
        return res

class Solution2(object):
    def longestPalindrome(self, s):
        if not s:
            return ''
        if len(s)==1:
            return s
        res = ''
        dp = [[True]*len(s) for _ in range(len(s))]
        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i][j] and j-i+1>len(res):
                    res = s[i:j+1]
        return res
    
if __name__ == "__main__":
    sl = Solution()
    s = 'a'
    print(sl.longestPalindrome(s))

                    
                