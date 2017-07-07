class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        right = 0
        while i <=right:
            right = max(right, i+nums[i])
            if right >= len(nums)-1:
                return True
            i += 1
        return False
