#所有与边界联通的'O'都不被包围，标记联通的'O',替换剩下的’O'
class Solution:
    def solve(self, board):
        row = len(board)
        col = len(board[0])
        def dfs(board,m,n,level):
            if m < 0 or n < 0 or m > row-1 or n > col-1:
                return
            if board[m][n] != 'O':
                return
            #做选择
            board[m][n] = 'A'
            dfs(board,m,n+1,level+1)
            dfs(board,m+1,n,level+1)
            dfs(board,m,n-1,level+1)
            dfs(board,m-1,n,level+1)

        for i in range(row):
            for j in range(col):
                if i==0 or i==row-1 or j==0 or j==col-1 and board[i][j] == 'O':
                    dfs(board,i,j,0)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        return board