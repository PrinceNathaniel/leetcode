# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recur(root,0)
    def recur(self, root, sums):
        if not root:
            return 0

        sums = root.val+sums*10
        return sum([self.recur(root.left, sums) ,self.recur(root.right, sums)]) or sums
        
