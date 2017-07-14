# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=0
        if not root:
            return res
        cur = [root]
        while cur:
        
            child=[]
            res += 1
            for node in cur:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
                if not node.left and not node.right:
                    return res
            cur = child
            
        return res
