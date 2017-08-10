# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.recur(1,n,{})
    def recur(self,low,high,saves):
        if (low,high) not in saves:
            l = []
            for root in range(low,high+1):
                for left in self.recur(low,root-1,saves):
                    for right in self.recur(root+1,high,saves):
                        node=TreeNode(root)
                        node.left = left
                        node.right = right
                        l.append(node)
            saves[(low,high)] = l
        return saves[(low,high)] or [None]
