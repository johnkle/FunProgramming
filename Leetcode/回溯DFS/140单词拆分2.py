class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        #记录s[i:]是否可以被拆分
        memo = [True]*len(s)
        def dfs(s,wordDict,begin,path):
            #回溯前先记下答案中有多少个元素
            num = len(res)
            if begin == len(s):
                res.append(' '.join(path.copy()))
                return
            for i in range(begin,len(s)):
                #判断s[begin:]是否可以被拆分
                if memo[begin] and s[begin:i+1] in wordDict:
                    path.append(s[begin:i+1])
                    dfs(s,wordDict,i+1,path)
                    path.pop()
            #res中的元素增加，说明s[pos:]可以分割，修改备忘录 
            memo[begin] = True if len(res)>num else False
            print(memo)
        dfs(s,wordDict,0,[])
        return res

class Solution1:
    def wordBreak(self, s, wordDict):
        res = []
        wordSet = set(wordDict)
        def dfs(s,wordSet,begin,path):
            if begin == len(s):
                res.append(' '.join(path.copy()))
                return
            for i in range(begin,len(s)):
                if not s[begin:i+1] in wordSet:
                    continue
                path.append(s[begin:i+1])
                dfs(s,wordSet,i+1,path)
                path.pop()
        dfs(s,wordSet,0,[])
        return res

class Solution2:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        #记录s[pos:]的拆分结果
        breakmap = dict()
        def dfs(s,wordSet,pos):
            if pos in breakmap:
                return breakmap[pos]
            if pos == len(s):
                return [[]]
            res = []
            for i in range(pos,len(s)):
                if s[pos:i+1] in wordSet:
                    word = s[pos:i+1]
                    nextBreaks = dfs(s,wordSet,i+1)
                    for x in nextBreaks:
                        res.append([word]+x.copy())
            breakmap[pos] = res
            return breakmap[pos]
        breakmap = dfs(s,wordSet,0)
        return [' '.join(words) for words in breakmap]

#动态规划？
class Solution5:
    def wordBreak(self, s, wordDict):
        dp = [['']]*(len(s)+1)
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] not in wordDict:
                    continue
                dp[i].append([x+' '+s[j:i] for x in dp[j]])
                #print(dp[i])
        print(dp)
        return dp[len(s)]

sl = Solution5()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
res = sl.wordBreak(s,wordDict)
print(res)

import copy
class Solution3:
    def wordBreak(self, s, wordDict):
        res = []
        #记录s[i:]是否可以被拆分
        memo = dict()
        def dfs(s,wordDict,begin,path):
            #res = []
            if begin in memo:
                return 
            if begin == len(s):
                res.append(path.copy())
                memo[begin] = res.copy()
                return
            for i in range(begin,len(s)):
                #判断s[begin:]是否可以被拆分
                if s[begin:i+1] in wordDict:
                    path.append(s[begin:i+1])
                    dfs(s,wordDict,i+1,path)
                    path.pop()
            #res中的元素增加，说明s[pos:]可以分割，修改备忘录 
            print(memo)
        dfs(s,wordDict,0,[])
        return memo

# sl = Solution3()
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# res = sl.wordBreak(s,wordDict)
# print(res)