class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) -1
        i,j = 0,right
        while i <= right:
            
            if nums[i] == 0:
                nums[left],nums[i] = nums[i],nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right],nums[i] = nums[i], nums[right]
                right -= 1
                i-= 1
            i +=1
