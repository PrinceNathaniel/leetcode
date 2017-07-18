class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pin2, pin = head, head
        while pin2 and pin2.next:
            pin, pin2 = pin.next, pin2.next.next
            if pin2 is pin:
                return True
        return False
