class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        res = [0]*m
        if grid[0][0]==0:
            res[0]=1
        for j in range(1,m):
            if grid[0][j] == 1:
                res[j] = 0
            else:
                res[j] = res[j-1]
        for i in range(1,n):
            if grid[i][0] == 1:
                res[0] = 0
            for j in range(1,m):
                if grid[i][j] == 1:
                    res[j] = 0
                else:
                    res[j] += res[j-1]
        return res[-1]
        
 
