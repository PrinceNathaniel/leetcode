# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur = [root]
        count = 1
        while cur:
            nextcur = []
            val = []
            for node in cur:
                val.append(node.val)
                if node.left:
                    nextcur.append(node.left)
                if node.right:
                    nextcur.append(node.right)
            if count %2 == 0:
                res.append(val[::-1])
            else:
                res.append(val)
            count += 1
            cur = nextcur
        return res
