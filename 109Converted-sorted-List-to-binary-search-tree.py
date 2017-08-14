# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        slow=ListNode(0)
        slow.next=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        node=TreeNode(slow.next.val)
        temp=slow.next.next
        slow.next=None
        node.left=self.sortedListToBST(head)
        node.right=self.sortedListToBST(temp)
        return node
