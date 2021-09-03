# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0]*len(s) for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]

# if __name__ == "__main__":
#     sl = Solution()
#     s = 'baac'
#     print(sl.longestPalindrome(s))

class Solution2(object):
    def longestPalindromeSubseq(self, s):
        if not s:
            return
        #dp[i][j]以索引i,j结尾的字符串的最长回文子序列长度
        #dp 数组全部初始化为 0
        dp = [[0]*len(s) for _ in range(len(s))]
        #base case
        for i in range(len(s)):
            dp[i][i] = 1
        #反着遍历保证正确的状态转移
        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][len(s)-1]

#返回最长子序列
def lps(s):
    if not s:
        return
    #dp[i][j]以索引i,j结尾的字符串的最长回文子序列
    #dp 数组全部初始化为 0
    dp = [['']*len(s) for _ in range(len(s))]
    #base case
    for i in range(len(s)):
        dp[i][i] = s[i]
    #反着遍历保证正确的状态转移
    for i in range(len(s)-2,-1,-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                dp[i][j] = s[i]+dp[i+1][j-1]+s[j]
            else:
                if len(dp[i+1][j])>len(dp[i][j-1]):
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[0][len(s)-1]

if __name__ == "__main__":
    s = "babad"
    print(lps(s))
