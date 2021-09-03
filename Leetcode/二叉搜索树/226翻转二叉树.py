class Solution(object):
    def invertTree(self, root):
        if not root:
            return
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left,root.right = root.right,root.left
        return root

class Solution2(object):
    def invertTree(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            node.left,node.right = node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root