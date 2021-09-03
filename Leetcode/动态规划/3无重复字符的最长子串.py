# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 注意最长和最短问题的区别，第二层循环
class Solution(object):
    def lengthOfLongestSubstring(self, s):
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

#dp[i] 以索引i结尾的最长子串
class Solution2:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dp = ['' for _ in range(len(s))]
        dp[0] = s[0]
        res = 0
        for i in range(1,len(dp)):
            idx = dp[i-1].find(s[i])
            if idx == -1:
                dp[i] = dp[i-1]+s[i]
            else:
                dp[i] = dp[i-1][idx+1:]+s[i]
            res = max(res,len(dp[i]))
        return res

            



if __name__ == "__main__":
    sl = Solution2()
    s = " "
    print(sl.lengthOfLongestSubstring(s))
