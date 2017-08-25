class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sindex,pindex,spre,ppre = 0,0,-1,-1
        while sindex<len(s):
            if pindex<len(p) and (s[sindex] == p[pindex] or p[pindex] == '?'):
                pindex += 1
                sindex += 1
            elif pindex<len(p) and p[pindex] == '*':
                pindex += 1
                ppre = pindex
                spre = sindex
            elif ppre!= -1:
                spre+=1
                sindex=spre
                pindex=ppre
            else:
                return False
        while pindex<len(p) and p[pindex] == '*':
                pindex+=1
        return pindex == len(p)
