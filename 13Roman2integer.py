class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"M":1000,"D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        res = 0
        for i in range(len(s)):
            if map[s[i]]>map[s[i-1]] and i>0:
                res -= map[s[i-1]]*2
            res += map[s[i]]
        return res
