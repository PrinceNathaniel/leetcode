class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        local, res = 0, float("-inf")
        for x in nums:
            local = max(0, local+x)
            res = max(res, local)
        return res
