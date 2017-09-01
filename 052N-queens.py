class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        self.recur([],[],[],res,n)
        return len(res)
    def recur(self,queens,diagnolsub,diagnoladd,res,n):
        if len(queens) == n:
            res.append(queens)
        y = len(queens)
        for x in range(n):
            if x not in queens and x-y not in diagnolsub and x+y not in diagnoladd:
                self.recur(queens+[x],diagnolsub+[x-y],diagnoladd + [x+y],res,n)
