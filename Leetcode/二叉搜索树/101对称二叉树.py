#先判断根节点，再判断左右子树是否对称
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left,root.right)
    def dfs(self,node1,node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        else:
            return node1.val==node2.val and\
                self.dfs(node1.left,node2.right) and self.dfs(node1.right,node2.left)

class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(nodeA,nodeB):
            if not nodeA:
                return not nodeB
            if not nodeB:
                return not nodeA
            return nodeA.val==nodeB.val and\
                dfs(nodeA.left,nodeB.right) and dfs(nodeA.right,nodeB.left)
        if not root:
            return True
        return dfs(root.left,root.right)