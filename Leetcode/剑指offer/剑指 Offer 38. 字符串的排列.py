#对原数组排序，保证相同的数字都相邻，然后每次填入的数一定是这个数所在重复数集合中「从左往右第一个未被填过的数字」
class Solution:
    def permutation(self, s):
        res = []
        used = [False]*len(s)
        def dfs(s,path):
            if len(path) == len(s):
                res.append(''.join(path))
                return
            for i in range(len(s)):
                if used[i]:
                    continue
                if i>0 and s[i]==s[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(s[i])
                dfs(s,path)
                path.pop()
                used[i] = False
        s = ''.join(sorted(s))
        dfs(s,[])
        return res