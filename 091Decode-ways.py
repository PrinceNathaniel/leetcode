class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        pre, pre2 = 1,0
        for i in range(len(s)):
            cur = 0
            if s[i] != '0':
                cur = pre
            if i>0 and (s[i-1]=='1' or (s[i-1] =='2' and s[i] <= '6') ):
                cur += pre2
            pre,pre2 = cur,pre
        return pre
