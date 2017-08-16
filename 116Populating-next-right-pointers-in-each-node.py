# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        cur = [root]
        while cur:
            nextcur = []
            for node in cur:
                if node.left:
                    nextcur.append(node.left)
                if node.right:
                    nextcur.append(node.right)
            for i in range(len(nextcur)-1):
                nextcur[i].next = nextcur[i+1]
            cur = nextcur
