# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,node))
        tmp = ListNode(-1)
        head = tmp
        while heap:
            smallestNode = heapq.heappop(heap)[1]
            tmp.next = smallestNode
            tmp = tmp.next
            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, smallestNode.next))
        return head.next
