# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (self.height(root)>=0)
    def height(self,root):
        if not root:
            return 0
        left, right = self.height(root.left), self.height(root.right)
        if left < 0 or right < 0 or abs(left-right)>1:
            return -1
        else:
            return max(left,right)+1
