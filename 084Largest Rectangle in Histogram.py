class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        n = len(heights)+1
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(n):
            while heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                wide = i - stack[-1] -1
                res = max(res,h*wide)
            stack.append(i)

        return res
                
