class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0
        right = 0 
        res = 0
        window = dict()
        while right < len(s):
            c = s[right]
            if c not in window:
                window[c] = 0
            window[c] += 1
            while window[c] > 1:
                window[s[left]] -= 1
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

                