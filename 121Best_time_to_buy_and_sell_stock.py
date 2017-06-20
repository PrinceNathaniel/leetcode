class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res, buyprice = 0, float("inf")
        for sellprice in prices:
            res = max(sellprice-buyprice, res)
            buyprice = min(buyprice, sellprice)
        return res
