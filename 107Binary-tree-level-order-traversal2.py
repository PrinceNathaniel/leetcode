# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, cur = [], [root]
        while cur:
            child, val = [], []
            for node in cur:
                val.append(node.val)
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            cur = child
            res.append(val)
        return res[::-1]
        
