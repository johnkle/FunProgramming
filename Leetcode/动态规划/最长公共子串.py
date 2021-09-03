#和最长公共子序列的区别
def lcs(text1, text2):
    m = len(text1)
    n = len(text2)
    #dp 数组的定义：对于text1[1..i]和text2[1..j]，LCS长度是dp[i][j]，且以text[i]和text[j]结尾
    #注意dp维度，外围包了一层0
    dp = [[0]*(n+1) for i in range(m+1)]
    res = 0
    #索引从1开始
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                res = max(res,dp[i][j])
    return res

if __name__ == "__main__":
    text1 = 'abcdef'
    text2 = 'bcd'
    print(lcs(text1,text2))