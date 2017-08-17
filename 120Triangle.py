class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        cur = n-2
        res =triangle[-1]
        while cur >=0:
            width = len(triangle[cur])
            for j in range(width):
                res[j] = triangle[cur][j]+min(res[j],res[j+1])
            cur-=1
        return res[0]
