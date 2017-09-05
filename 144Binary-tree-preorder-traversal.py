# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recur(root,res)
        return res
    def recur(self,root,res):
        if not root:
            return None
        res.append(root.val)
        self.recur(root.left,res)
        self.recur(root.right,res)
