# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.recur(root,sum,[],res)
        return res
    def recur(self, root, sum,l,res):
        if not root:
            return
        if sum == root.val and (root.left is None and root.right is None):
            l.append(root.val)
            res.append(l)
        tmp = root.val
        self.recur(root.left,sum-tmp,l+[tmp],res)
        self.recur(root.right,sum-tmp,l+[tmp],res)
