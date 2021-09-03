class Solution(object):
    def rightSideView(self, root):
        res = []
        temp = []
        queue = []
        queue.append([root,0])
        if not root:
            return []
        while queue:
            cur = queue.pop(0)
            node = cur[0]
            level = cur[1]
            #体会这条语句的含义
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
        for r in res:
            temp.append(r[-1])
        return temp

class Solution2(object):
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if i == length-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res