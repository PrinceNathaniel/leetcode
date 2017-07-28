class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 1 if n>0 else -1
        n = abs(n)
        res = 1
        while n>0 :
            if n %2==1:
                res *= x
            n>>=1
            x *= x
        if flag < 0 :
            res = 1/res
        return res
