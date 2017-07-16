class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
#method2:
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in nums[1:]:
            result ^= i
        return result
