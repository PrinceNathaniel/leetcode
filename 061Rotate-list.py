# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        n,cur = 1, head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head
        cur = head
        tail = cur
        for __ in range(n-k%n):
            tail = cur
            cur = cur.next
        tail.next = None

        
        return cur
