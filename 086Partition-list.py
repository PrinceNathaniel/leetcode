# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1, dummy2 = ListNode(0), ListNode(0)
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p1,p2 = dummy1,dummy2
        while pre.next:
            cur = pre.next
            if cur.val <x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next
            pre = pre.next
        p2.next = None
        p1.next = dummy2.next
        return dummy1.next
                
