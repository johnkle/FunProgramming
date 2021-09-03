import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub('  +',' ',s.strip()).split(' ')
        left = 0
        right = len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return ' '.join(s)

class Solution2:
    def reverseWords(self, s):
        s = re.sub('  +',' ',s.strip()).split(' ')
        return ' '.join(reversed(s))

if __name__ == '__main__':
    sl = Solution()
    s = "  Bob    Loves  Alice   "
    res = sl.reverseWords(s)
    print(res)