class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        res[0][0]=True
        for i in range(2, len(p)+1):
            if p[i-1]=='*':
                res[0][i] = res[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] != '*':
                    res[i][j] = res[i-1][j-1] and (s[i-1]== p[j-1] or p[j-1]=='.')
                else:
                    res[i][j] = res[i][j-2] or (res[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
        return res[len(s)][len(p)]
