class Solution:
    def verifyPostorder(self, postorder):
        def dfs(left,right):
            #终止条件
            if left>=right:
                return True
            i = left
            #寻找第一个大于root值的节点，并验证左子树
            while postorder[i] < postorder[right]:
                i += 1
            #验证右子树
            j = i
            while postorder[i] > postorder[right]:
                i += 1
            return i==right and dfs(left,j-1) and dfs(j,right-1)
        return dfs(0,len(postorder)-1)