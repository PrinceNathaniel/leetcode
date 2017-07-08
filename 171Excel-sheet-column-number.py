class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            number = (ord(s[-1-i])-64)
            res += number*(26**i)
        return res
