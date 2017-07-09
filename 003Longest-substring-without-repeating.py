class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <2:
            return len(s)
        locations = [-1 for i in range(256)]
        index, res = -1, 0
        for i, char in enumerate(s):
            if locations[ord(char)]> index:
                index = locations[ord(char)]
            res = max(res, i-index)
            locations[ord(char)] = i
        return res
