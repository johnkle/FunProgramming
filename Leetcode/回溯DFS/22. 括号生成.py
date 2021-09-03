class Solution:
    def generateParenthesis(self, n):
        res = []
        def dfs(n,left,right,path):
            if left==n and right==n:
                res.append(''.join(path.copy()))
                return
            if left < n:
                path.append('(')
                dfs(n,left+1,right,path)
                path.pop()
            if right < left:
                path.append(')')
                dfs(n,left,right+1,path)
                path.pop()
        dfs(n,0,0,[])
        return res

#这个回溯过程不太理解但是成功了
class Solution2:
    def generateParenthesis(self, n):
        res = []
        def dfs(n,left,right,path):
            if left==n and right==n:
                res.append(''.join(path.copy()))
                return
            if left < right:
                return
            if left < n:
                path.append('(')
                print('left之前',path)
                dfs(n,left+1,right,path)
                path.pop()
                print('left之后',path)
            if right < n:
                path.append(')')
                print('right之前',path)
                dfs(n,left,right+1,path)
                path.pop()
                print('right之后',path)
        dfs(n,0,0,[])
        return res


