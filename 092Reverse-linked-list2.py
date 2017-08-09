# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prem = dummy
        count = 1
        while cur and m!=count:
            count += 1
            prem, cur = cur, cur.next
        pre = prem
        mnode = cur
        while cur and n!= count-1:
            count += 1
            cur.next,pre,cur = pre, cur, cur.next
        
        prem.next = pre
        mnode.next = cur
        return dummy.next
            
