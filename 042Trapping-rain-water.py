class Solution(object):
    def trap(self, a):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(a) <3:
            return 0
        left, right = 0, len(a) -1
        block , res = 0, 0
        while left < right:
            if a[left]<a[right]:
                minh = a[left]
                left += 1
            else:
                minh = a[right]
                right -= 1
            block = max(block, minh)
            res += block - minh
        return res
