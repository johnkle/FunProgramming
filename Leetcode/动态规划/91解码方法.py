#dp[i]表示s[...i]解码方法总数
class Solution(object):
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1,len(s)):
            #s[i]为'0'的情况
            if s[i] == '0':
                if s[i-1]=='1' or s[i-1]=='2':
                    dp[i] = dp[i-2] if i-2>=0 else 1
            #s[i]不为'0'
            else: 
                #s[i-1..i]两位数<=26的情况
                if s[i-1] == '1' or (s[i-1]=='2' and '1'<=s[i]<='6'):
                    dp[i] = dp[i-1]+dp[i-2] if i-2>=0 else 2
                #其他情况
                else:
                    dp[i] = dp[i-1]
        return dp[len(s)-1]



class Solution2:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        res = []
        #memo = [True]*len(s)
        def dfs(s,begin,path):
            #num = len(s)
            if begin == len(s):
                res.append(path.copy())
                return
            for i in range(begin,len(s)):
                # if not memo[begin]:
                #     continue
                if 1<=int(s[begin:i+1])<=26 and s[begin]!='0':
                    path.append(s[begin:i+1])
                    dfs(s,i+1,path)
                    path.pop()
            #memo[begin] = True if len(res)>num else False
        dfs(s,0,[])
        #print(memo)
        return res


class Solution3:
    def numDecodings(self, s: str) -> int:
        breakmap = dict()
        def dfs(s,pos):
            if pos in breakmap:
                return breakmap[pos]
            if pos == len(s):
                return [[]]
            res = []
            for i in range(pos,len(s)):
                if 1<=int(s[pos:i+1])<=26 and s[pos]!='0':
                    word = s[pos:i+1]
                    nextbreaks = dfs(s,i+1)
                    for x in nextbreaks:
                        res.append([word]+x)
            breakmap[pos] = res
            return breakmap[pos]
        return len(dfs(s,0))

sl = Solution3()
s = "123"
res = sl.numDecodings(s)
print(res)

