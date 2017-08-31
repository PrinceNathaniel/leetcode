class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0]*n
        right = [n]*n
        height = [0]*n
        res = 0
        for row in range(m):
            curleft, curright = 0, n
            for i in range(n):
                if matrix[row][i] == '1':
                    height[i] += 1
                    left[i] = max(left[i],curleft)
                else:
                    curleft  = i+1
                    left[i] = 0
                    height[i] = 0
            for i in reversed(range(n)):
                if matrix[row][i] == '1':
                    right[i] = min(right[i],curright)
                else:
                    curright = i
                    right[i] = n
            for i in range (n):
                res= max(res,(right[i]-left[i])*height[i])
        return res
