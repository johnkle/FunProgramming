# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if len(res)%2 == 0:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res