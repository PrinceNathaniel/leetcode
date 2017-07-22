class Solution(object):
    dirphone={'2':'abc','3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        res = []
        self.dfs(digits, '', res)
        return res
    def dfs(self, digits,cur,res):
            if not digits:
                res.append(cur)
                return
            for char in self.dirphone[digits[0]]:
                self.dfs(digits[1:], cur + char, res)
