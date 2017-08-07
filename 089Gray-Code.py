class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res= [(i>>1)^i for i in xrange(pow(2,n))]
        return res
