class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        self.recur(s,0,[],res)
        return res
    def recur(self,s,n,l,res):
        if not s:
            if n == 4:
                res.append('.'.join(l))
            return
        elif n == 4:
            return
        self.recur(s[1:],n+1,l+[s[0]],res)
        if s[0] !='0':
            if len(s)>=2:
                self.recur(s[2:],n+1,l+[s[:2]],res)
            if len(s)>=3 and int(s[:3])<256:
                self.recur(s[3:], n+1, l+[s[:3]], res)
