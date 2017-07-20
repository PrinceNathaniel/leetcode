# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cura, curb = headA, headB
        taila, tailb = None, None
        while cura and curb:
            if cura == curb:
                return cura
            
            if cura.next:
                cura = cura.next
            elif taila is None:
                taila = cura
                cura = headB
            else:
                break
            if curb.next:
                curb = curb.next
            elif tailb is None:
                tailb = curb
                curb = headA
            else:
                break
