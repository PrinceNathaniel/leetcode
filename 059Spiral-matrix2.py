class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left, right, up, down = 0,n-1,0,n-1
        res = [[0 for __ in range(n)]for __ in range(n)]
        count = 0
        while left<right and up < down:
            for j in range(left,right):
                count += 1
                res[up][j] = count
            for i in range(up,down):
                count +=1
                res[i][right] = count
            for j in reversed(range(left+1, right+1)):
                count += 1
                res[down][j] = count
            for i in reversed(range(up+1,down+1)):
                count += 1
                res[i][left] = count
            left,right,up,down = left+1,right-1,up+1,down-1
        if n%2 ==1:
            res[left][up] = count +1
        return res
        
