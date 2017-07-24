class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = 1
        if dividend >= 0 and divisor < 0 or dividend <= 0 and divisor > 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        cur = divisor
        count = 1
        while dividend>=cur:
            cur <<=1
            count <<=1
        while dividend>=divisor:
            cur >>=1
            count >>=1
            if cur<=dividend:
                dividend -= cur
                res += count
        return min(2147483647, sign*res)
        
