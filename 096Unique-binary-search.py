class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1 for i in range(n+1) ]

        for i in range(1,n+1):
            s= 0
            for j in range(1,i+1):
                s += res[j-1]*res[i-j]
            res[i] = s
        return res[-1]
