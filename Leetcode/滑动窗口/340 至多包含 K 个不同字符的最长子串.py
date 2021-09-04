class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0
        window = dict()
        res = ''
        while right < len(s):
            c = s[right]
            if c not in window:
                window[c] = 0
            window[c] += 1
            while len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
            if right-left+1 > len(res):
                res = s[left:right+1]
            right += 1
        return len(res)