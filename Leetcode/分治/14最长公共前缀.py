class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        #初始化公共前缀
        temp = strs[0]
        #两两找出最长公共前缀
        for i in range(1, len(strs)):
            while strs[i].find(temp) != 0:
                temp = temp[:-1]
        return temp
#分治
class Solution2:
    def longestCommonPrefix(self, strs):
        def lcp(strs,left,right):
            if left == right:
                return strs[left]
            mid = left + (right-left)//2
            lcpleft = lcp(strs,left,mid)
            lcpright = lcp(strs,mid+1,right)
            #merge
            minlen = min(len(lcpleft),len(lcpright))
            for i in range(minlen):
                if lcpleft[i] != lcpright[i]:
                    return lcpleft[:i]
            #注意，遍历之后左右前缀值都相等，返回
            return lcpleft[:minlen]
        return lcp(strs,0,len(strs)-1)
#dp
class Solution3(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        #strs[0:i]最长公共前缀
        dp = [strs[0] for _ in range(len(strs))]
        for i in range(len(strs)):
            while not strs[i].startswith(dp[i-1]):
                dp[i-1] = dp[i-1][:-1]
            dp[i] = dp[i-1]
        return dp[-1]