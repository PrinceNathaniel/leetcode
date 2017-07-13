class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix ==[]:
            return res
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left<= right and up<= down:
            for j in range(left, right +1):
                res.append(matrix[up][j])
            for i in range(up+1,down+1):
                res.append(matrix[i][right])
            for j in reversed(range(left, right)):
                if up<down:
                    res.append(matrix[down][j])
            for i in reversed(range(up+1,down)):
                if left<right:
                    res.append(matrix[i][left])
            left, right, up, down = left +1, right -1, up +1, down -1
        return res
