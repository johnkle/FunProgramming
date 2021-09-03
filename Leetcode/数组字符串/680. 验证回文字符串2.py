class Solution:
    def validPalindrome(self, s):
        def check(s):
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]==s[right]:
                left += 1
                right -= 1
            else:
                return check(s[left+1:right+1]) or check(s[left:right])
        return True