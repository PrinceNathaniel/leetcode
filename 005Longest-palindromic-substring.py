class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '@'+'@'.join(s)+'@'
        
        seq=[0]*len(s)
        rightrange, axis, maxlen = 0, 0, 0
        for i in range(len(s)):
            if i < rightrange:
                seq[i]= min(seq[2*axis-i], rightrange-i)
            else:
                seq[i] = 1
            while i - seq[i] >=0 and i + seq[i]<len(s) and s[i-seq[i]]==s[i+seq[i]]:
                seq[i] += 1
            if seq[i] + i -1 > rightrange:
                rightrange = seq[i] + i -1
                axis = i
            maxlen = max(maxlen, seq[i])
        key = seq.index(maxlen)
        
        if s[key] == '@':
            flag = 1
            res = ''
        else:
            flag = 2
            res = s[key]
        for i in range(flag,maxlen,2):
            res = s[key+i]+res+s[key+i]
        return res
