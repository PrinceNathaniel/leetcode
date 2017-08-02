class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m= len(matrix[0])
        n = len(matrix)
        left, right = 0, m*n-1
        while left<=right:
            mid = (left+right)/2
            key = matrix[mid/m][mid%m]
            if target > key:
                left = mid+1
            elif target < key:
                right = mid-1
            else:
                return True
        return False
