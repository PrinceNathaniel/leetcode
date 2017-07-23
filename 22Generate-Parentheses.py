class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.recur(n,n,'',res)
        return res
    def recur(self,left,right,l,res):
        if left == 0 and right == 0:
            res.append(l)
        if left > 0:
            self.recur(left-1,right,l+'(', res)
        if right > left:
            self.recur(left,right-1,l+')', res)
            
        
