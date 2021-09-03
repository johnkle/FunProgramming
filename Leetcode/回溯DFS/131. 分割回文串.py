class Solution:
    def partition(self, s):
        res = []
        def dfs(s,begin,path):
            if begin==len(s):
                res.append(path.copy())
            for i in range(begin,len(s)):
                if not check(s[begin:i+1]):
                    continue
                path.append(s[begin:i+1])
                dfs(s,i+1,path)
                path.pop()
        def check(s):
            return s == s[::-1]
        dfs(s,0,[])
        return res
