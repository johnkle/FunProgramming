import collections
class Solution(object):
    def levelOrder(self, root):
        res = []
        queue = []
        if not root:
            return []
        queue.append([root,0])
        while queue:
            cur = queue.pop(0)
            node = cur[0]
            level = cur[1]
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
        return res

class Solution2:
    def levelOrder(self, root):
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res



