#超时
class Solution:
    def minCut(self, s: str) -> int:
        self.res = len(s)+1
        def dfs(s,pos,path):
            if pos==len(s):
                self.res = min(self.res,len(path))
                return
            for i in range(pos,len(s)):
                if not check(s[pos:i+1]):
                    continue
                path.append(s[pos:i+1])
                dfs(s,i+1,path)
                path.pop()
        def check(s):
            return s==s[::-1]
        dfs(s,0,[])
        return self.res-1

if __name__ == "__main__":
    sl = Solution()
    s = 'fff'
    res = sl.minCut(s)
    print(res)