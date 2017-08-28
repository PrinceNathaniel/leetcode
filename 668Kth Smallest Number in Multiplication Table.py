class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def bigenough(x):
            return sum(min(x/i,n) for i in range(1,m+1))>=k
        start,end = 1, m*n
        while start<end:
            mid = (start+end)/2
            if bigenough(mid):
                end = mid
            else:
                start = mid+1
        return end
        
