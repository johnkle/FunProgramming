class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root,p,q):
            if not root:
                return
            if p.val==root.val or q.val==root.val:
                return root
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            if not left:
                return right
            if not right:
                return left
            return root
        return dfs(root,p,q)