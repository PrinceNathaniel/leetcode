class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_number= int(''.join([str(x) for x in digits]))+1
        return [int(i) for i in str(int_number)]
