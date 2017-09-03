class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
            
        if n>=4:
            if m>2:
                return 8
            elif m ==2:
                return 7
            elif m == 1:
                return 4
        elif n ==3:
            if m>2:
                return 8
            elif m ==2:
                return 7
            elif m == 1:
                return 4
        elif n == 2:
            if m>=2:
                return 4
            elif m == 1:
                return 3
        elif n == 1:
            return 2
