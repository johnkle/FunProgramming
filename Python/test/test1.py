# arr = [[1,2,3,4,5] for _ in range(5)]
# print(arr)
# for i in range(3,-1,-1):
#     for j in range(i+1,5):
#         print([i,j])

# flag = 1
# for i in range(3):
#     for j in range(6,10):
#         if j==8:
#             continue
#         flag = 0
#         print(j)
#     if flag == 0:
#         break
# s1 = 'abc'
# print(s1[::-1])
# nums = [1,2,3,0,0]
# print(nums.index(2))
#print([i for i in nums if i !=0])
# print(list(filter(lambda x:x>0,nums)))
# print(list(map(lambda x:x*2,nums)))
# dp = [1]*3
# for i in range(1,3):
#     dp[i] = 1/2*dp[i-1]
# print(dp)

# nums = [1,2,3]
# print(nums.pop(-1))
# print(nums)
# nums.insert(0,5)
# print(nums)
# s ='abc'
# print(s.find('b'))

lists = [[1,4,5],[1,3,4],[2,6]]
temp = []
# new_lists = [temp.extend(x) for x in lists]
# print(new_lists)
# print([[1]*3 for _ in range(2)])

def lcs(text1, text2):
    m = len(text1)
    n = len(text2)
    #dp 数组的定义：对于text1[1..i]和text2[1..j]，LCS长度是dp[i][j]
    #注意dp维度，外围包了一层0
    dp = [[0]*(n+1) for i in range(m+1)]
    maxLen = 0
    #索引从1开始
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            if dp[i][j]>maxLen:
                maxLen = dp[i][j]
    return maxLen 

def lcs2(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0]*(n) for i in range(m)]
    maxLen = 0
    for i in range(0,m):
        for j in range(0,n):
            if text1[i] == text2[j]:
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1]+1
            if dp[i][j]>maxLen:
                maxLen = dp[i][j]
    return maxLen 
text1 = 'abcde'
text2 = 'acdedefe'



def longestPalindrome(s):
    if not s:
        return ''
    if len(s) == 1:
        return s
    length = 0
    res = ''
    dp = [[True]*len(s) for _ in range(len(s))]
    for i in range(len(s)-2,-1,-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
            if dp[i][j]==True:
                length = j-i+1
                res = s[i:j+1]
                print(res)
                print(length)
    return dp

s = 'ac'
dp = longestPalindrome(s)
#print(longestPalindrome(s))
# res = ''
# length = 0
# for i in range(len(dp)):
#     for j in range(len(dp)):
#         if dp[i][j]==True and j-i+1>length:
#             length = j-i+1
#             res = s[i:j+1]
# print(res)


def numDecodings(s):
    if s[0] == '0':
        return 0
    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    for i in range(1,len(s)):
        if s[i] == '0':
            if s[i-1]=='1' or s[i-1]=='2':
                dp[i] = dp[i-2] if i-2>=0 else 1
        else: 
            if s[i-1] == '1' or (s[i-1]=='2' and '1'<=s[i]<='6'):
                dp[i] = dp[i-1]+dp[i-2] if i-2>=0 else 2
            else:
                dp[i] = dp[i-1]
    return dp





def permutation(s):
    res = []
    used = [False]*len(s)
    def dfs(s,path):
        if len(path) == len(s):
            res.append(path)
            return
        for i in range(len(s)):
            if used[i]:
                continue
            if i>0 and s[i]==s[i-1]:
                continue
            used[i] = True
            path += s[i]
            print("递归之前",path)
            dfs(s,path)
            path = path[:-1]
            print("递归之后",path)
            used[i] = False
    dfs(s,'')
    return res


s = '1135'
def check(s):
    if s == '0':
        return True
    elif '1'<=s<='255' and not s.startswith('0'):
        return True
    return False
# print(check(s))


def f():
    a = 0
    for i in '123':
        a += int(i)
    print(a)
f()

print(3)
print([False]*3)
lst = [False]*3
lst[0]=1

print(lst)
print(lst)
print(lst)
print(lst)
