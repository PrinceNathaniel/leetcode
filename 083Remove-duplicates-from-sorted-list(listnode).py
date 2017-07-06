# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            nextone = cur.next
            while nextone and nextone.val == cur.val:
                nextone = nextone.next
            cur.next = nextone
            cur = nextone
        return head
