import collections
class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        left = 0
        right = 0
        window = collections.defaultdict(int)
        res = 0
        while right < len(s):
            c = s[right]
            window[c] += 1
            #与无重复最长子串区别
            while window[c] > 1 or right-left+1>k:
                window[s[left]] -= 1
                left += 1
            if right-left+1 == k:
                res += 1
            right += 1
        return res

class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        left = 0
        right = k-1
        window = collections.Counter(s[:k])
        res = 0
        while right < len(s):
            if len(window) == k:
                res += 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                window.pop(s[left])
            left += 1
            right += 1
            if right < len(s):
                window[s[right]] += 1
        return res