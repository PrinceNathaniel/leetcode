class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1:
            return 1
        elif not nums:
            return 0
        res =1
        count =1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                res=max(res,count)
                count = 1
        return max(res,count)
