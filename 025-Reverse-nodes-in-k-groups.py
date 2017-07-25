# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = ListNode(-1)
        pre.next = head
        cur = head
        begin = pre
        n = 0
        while cur:
            end = cur.next
            n = (n+1)%k
            if n == 0:
                next_begin = begin.next
                self.reverse(begin,end)
                begin = next_begin
            cur = end
        return pre.next
    def reverse(self, begin, end):
        node1 = begin.next
        node2 = node1.next
        while node2 != end:
            node1.next = node2.next
            node2.next = begin.next
            begin.next = node2
            node2 = node1.next
        
    
