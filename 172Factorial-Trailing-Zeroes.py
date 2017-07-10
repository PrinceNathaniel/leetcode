class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        res = 0
        while m <= n:
            m *= 5
            res += n/m
        return res
