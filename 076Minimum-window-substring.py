class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        times = collections.Counter(t)
        miss = len(t)
        i,left,right = 0,0,0
        for j,c in enumerate(s,1):
            
            miss-=times[c]>0
            times[c]-= 1
            if not miss:
                while i < j and times[s[i]]<0:
                    times[s[i]]+=1
                    i+=1
                if not right or j-i<=right-left:
                    left,right = i,j
        return s[left:right]
