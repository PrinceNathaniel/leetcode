# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(-1)
        pre.next = head
        tmp = pre
        while tmp.next and tmp.next.next:
            node1=tmp.next
            node2 = tmp.next.next
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = tmp.next.next
        return pre.next
