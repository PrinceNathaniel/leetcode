class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = [i for i in s.lower() if i.isalnum()]
        return res == res[::-1]
