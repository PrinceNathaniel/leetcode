class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix[0])
        n = len(matrix)
        #lend  a row and a column
        flagj,flagi = 1, 1
        for i in range(n):
            if matrix[i][0]==0:
                flagi = 0
        for j in range(m):
            if matrix[0][j] == 0:
                flagj = 0
        #zeros the middle
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0],matrix[0][j] =0, 0
        for i in range (1,n):
            if matrix[i][0] == 0:
                for j in range(1,m):
                    matrix[i][j] = 0
        for j in range(1,m):
            if matrix[0][j] ==0:
                for i in range(1,n):
                    matrix[i][j] = 0
        #zeros the lent
        if flagi == 0:
            for i in range(n):
                matrix[i][0] = 0 
        if flagj == 0:
            for j in range(m):
                matrix[0][j] = 0
        
