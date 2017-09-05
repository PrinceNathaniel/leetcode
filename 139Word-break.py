class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #wordDict=set(wordDict)
        n = len(s)
        res = [False]*n
        for i in range(n):
            for j in range(i+1):
                if (res[j] and s[j+1:i+1] in wordDict) or s[:i+1] in wordDict:
                    res[i] = True
                    break
        return res[-1]
