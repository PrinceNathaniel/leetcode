# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        cur = [root]
        minest = root.val
        while cur:
            res =[]
            nextcur = []
            for node in cur:
                if node.left:
                    nextcur.append(node.left)
                    nextcur.append(node.right)
                if node.val != minest:
                    res.append(node.val)
            cur = nextcur
        if len(res)>0:
            return min(res)
        else:
            return -1
