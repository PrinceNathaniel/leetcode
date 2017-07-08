class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right, res = 0, 0
        reach = 0
        for i in range(len(nums)):
            if right < i:
                res += 1
                right = reach
            reach = max(reach, nums[i]+i)
        return res
