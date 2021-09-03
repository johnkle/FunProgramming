# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [[root,0]]
        res = []
        while queue:
            cur = queue.pop(0)
            node = cur[0]
            level = cur[1]
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
        return res

class Solution2(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [[root,0]]
        res = dict()
        while queue:
            cur = queue.pop(0)
            node = cur[0]
            level = cur[1]
            if level not in res:
                res[level] = []
            res[level].append(node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
        return list(res.values())


class Solution3(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [[root,0]]
        res = []
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                node = cur[0]
                level = cur[1]
                if len(res) <= level:
                    res.append([])
                res[level].append(node.val)
                if node.left:
                    queue.append([node.left,level+1])
                if node.right:
                    queue.append([node.right,level+1])
        return res
        