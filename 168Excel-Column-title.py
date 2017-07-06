class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        base = ord('A')
        while n:
            r = (n-1)%26
            n = (n-1)/26
            res.append(chr(base + r))
        return ''.join(res[::-1])
