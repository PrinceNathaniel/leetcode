class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i+1] for i in range(n)]
        res = []
        if n>k:
            res = [j+[n] for j in self.combine(n-1,k-1)]+self.combine(n-1,k)
        else:
            res = [j+[n] for j in self.combine(n-1,k-1)]
        return res
        
