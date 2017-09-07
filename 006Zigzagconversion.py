class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        l = ['']*numRows
        i = 0
        count = 1
        for char in s:
            l[i] += char
            if i ==0:
                count =1
            elif i == numRows-1:
                count =-1
            i+=count
        return ''.join(l)
