class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre, now = 1, 2
        for i in range(1,n):
            pre, now = now, pre + now
        return pre
