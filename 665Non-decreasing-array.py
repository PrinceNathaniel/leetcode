class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return True
        count,count2 = -1,-1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count = i-1
                count2 = i
                break
        i = count2
        nums1 = nums[:i-1]+nums[i:]
        nums2 = nums[:i]+nums[i+1:]
        if self.check(nums1) or self.check(nums2):
            return True
        return False
    def check(self,nums):
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                return False
        return True
