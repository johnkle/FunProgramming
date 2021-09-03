class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        left = 0
        right = 0
        window = dict()
        res = 0
        while right < len(s):
            c = s[right]
            if c not in window:
                window[c] = 0
            window[c] += 1
            while len(window) > 2:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res