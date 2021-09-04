class Solution:
    def findSubstring(self, s: str, words):
        def check(window,words):
            dp = [False]*(length+1)
            dp[0] = True
            for word in words:
                for i in range(len(window), len(word) - 1, -1):
                    if window[i - len(word):i] == word:
                        dp[i] |= dp[i - len(word)]
            #print(dp)
            return dp[-1]
        length = len(words)*len(words[0])
        left = 0
        right = length-1
        res = []
        while right < len(s):
            if check(s[left:right+1],words):
                res.append(left)
            #print(s[left:right+1])
            left += 1
            right += 1
        return res