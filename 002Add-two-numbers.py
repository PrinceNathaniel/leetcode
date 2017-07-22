# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cur, carry = res, 0
        while l1 or l2:
            tmp = carry
            if l1:
                tmp += l1.val
                l1=l1.next
            if l2:
                tmp += l2.val
                l2=l2.next
            tmp, carry = tmp%10, tmp/10
            cur.next = ListNode(tmp)
            cur = cur.next
            
        if carry == 1:
            cur.next = ListNode(1)
        return res.next
                
        
