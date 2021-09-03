class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for c in set(s):
            #子串必不包含小于K的c, 按c分段, 在各分段中找最长子串
            if s.count(c) < k:
                res = 0
                for part in s.split(c):
                    res = max(res,self.longestSubstring(part,k))
                return res
        #终止条件,遍历结束都>k,字符串无法再分割了
        return len(s)