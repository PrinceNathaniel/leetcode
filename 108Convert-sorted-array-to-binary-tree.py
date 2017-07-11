# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        left, right = 0, len(nums)
        return self.bintree(nums,left,right)
    def bintree(self, nums, left,right):
        if left == right:
            return None
        mid = (left+right)/2
        root = TreeNode(nums[mid])
        root.left = self.bintree(nums,left,mid)
        root.right = self.bintree(nums,mid+1,right)
        return root
