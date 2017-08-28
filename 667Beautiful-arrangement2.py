class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = range(1,n-k)
        for i in range(k+1):
            if i%2==0:
                res.append(n-k+i/2)
            else:
                res.append(n-i//2)
        return res
