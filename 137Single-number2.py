class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones^num)&~twos
            twos = (twos^num)&~ones
        return ones
        
        #method2
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(0,len(nums)-1,3):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
