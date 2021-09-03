import collections
class Solution:
    def canPermutePalindrome(self, s: str):
        lookup = collections.Counter(s)
        res = 0
        for x in lookup.values():
            res += x//2*2
            if x%2 == 1 and res%2==0:
                res += 1
        return res == len(s)