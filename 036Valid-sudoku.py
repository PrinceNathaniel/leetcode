class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValidList([board[i][j] for j in range(9)]) or not self.isValidList([board[j][i] for j in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValidList([board[m][n] for m in range(3*i,3*i+3) for n in range(3*j,3*j+3)]):
                    return False
        return True
    def isValidList(self, lists):
        lists = filter(lambda x:x!='.',lists)
        return len(set(lists))==len(lists)
#mehod 2 (faster)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = []
        for i,row in enumerate(board):
            for j,nums in enumerate(row):
                if nums != '.':
                    res += [(nums,j),(i,nums),(nums,i/3,j/3)]
        #return res
        return len(res) == len(set(res))
