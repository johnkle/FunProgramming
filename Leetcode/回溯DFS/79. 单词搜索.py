# https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-hui-su-suan-fa-jian-zhi-v-0vbd/
class Solution:
    def __init__(self):
        self.flag = False
    def exist(self, board, word):
        if not board or not board[0]:
            return
        res = []
        row = len(board)
        col = len(board[0])
        visited = [[False]*col for _ in range(row)]
        def dfs(board,m,n,level,path):
            if ''.join(path) == word:
                self.flag = True
                return
            #若超越边界或当前位置已访问，减枝
            if m<0 or n<0 or m>row-1 or n>col-1 or visited[m][n]:
                return
            #若当前位置的字符已经与要搜索的目标字符不同，减枝
            if board[m][n] != word[level]:
                return
            # if len(path) > len(word):
            #     return
            visited[m][n] = True
            path.append(board[m][n])
            dfs(board,m,n+1,level+1,path)
            dfs(board,m+1,n,level+1,path)
            dfs(board,m,n-1,level+1,path)
            dfs(board,m-1,n,level+1,path)
            path.pop()
            visited[m][n] = False
        #注意for循环位置，表示从[i,j]开始搜索，这样搜索路径是连续的
        for i in range(row):
            for j in range(col):
                dfs(board,i,j,0,[])
        return self.flag