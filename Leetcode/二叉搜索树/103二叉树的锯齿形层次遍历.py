class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
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
            if level%2==0:
                res[level].append(node.val)
            else:
                res[level].insert(0,node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
        return res