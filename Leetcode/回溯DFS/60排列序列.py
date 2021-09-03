import math
class Solution:
    def getPermutation(self, n, k):
        self.res = []
        self.num = 0
        used = [False]*(n+1)
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        #cnt = factorial[n-1]
        def dfs(n,k,idx,path):
            if idx==n:
                self.num += 1
                if self.num == k:
                    self.res = ''.join(path)
                return
            cnt = factorial[n - 1 - idx]
            for i in range(1,n+1):
                if cnt < k:
                    k -= cnt
                    #self.num += cnt
                    continue
                if used[i]:
                    continue
                used[i] = True
                path.append(str(i))
                dfs(n,k,idx+1,path)
                path.pop()
                used[i] = False
        dfs(n,k,0,[])
        return self.res

class Solution2:
    def getPermutation(self, n, k):
        self.res = []
        self.num = 0
        used = [False]*(n+1)
        def mul(n):
            if n<=1:
                return 1
            else:
                return n*mul(n-1)
        cycle = math.ceil(k/mul(n-1))-1
        k = k-cycle*(mul(n-1))
        def dfs(n,k,idx,path):
            if idx==n:
                self.num += 1
                if self.num == k:
                    self.res = ''.join(path)
                return
            for i in range(1,n+1):
                if used[i]:
                    continue
                used[i] = True
                path.append(str(i))
                dfs(n,k,idx+1,path)
                path.pop()
                used[i] = False
        dfs(n,k,0,[])
        return self.res

sl = Solution2()
res = sl.getPermutation(3,3)
print(res)