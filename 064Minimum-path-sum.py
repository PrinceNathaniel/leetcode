class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        res = [0]*m
        res[0] = grid[0][0]
        for j in range(1,m):
            res[j] = res[j-1]+grid[0][j]
        
        for i in range(1,n):
            res[0] += grid[i][0]
            for j in range(1,m):
                res[j] = min(res[j-1],res[j])+grid[i][j]
        
        return res[-1]
        
