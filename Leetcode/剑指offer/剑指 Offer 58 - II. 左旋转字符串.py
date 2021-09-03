from collections import deque
class Solution(object):
    def reverseLeftWords(self, s, n):
        n = n%len(s)
        lst = deque(s)
        lst.rotate(-n)
        return ''.join(lst)

sl = Solution()
s = "abcdefg"
n = 2
ret = sl.reverseLeftWords(s,n)
print(ret)