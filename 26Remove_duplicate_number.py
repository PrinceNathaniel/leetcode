class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        temp = 0
        for i in range(len(nums)):
            if nums[i] != nums[temp]:
                nums[res] = nums[i]
                res += 1
                temp = i
                
        return res
            
