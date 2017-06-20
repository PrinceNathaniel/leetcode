class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1, buy2 = float("inf"), float("-inf")
        sell1, sell2 = 0, 0
        for i in prices:
            sell2 = max(sell2, buy2+i)
            buy2 = max(buy2, sell1-i)
            sell1 = max(sell1, -buy1+i)
            buy1 = min(buy1, i)
        return sell2
        
        #time O(n) space O(1)
