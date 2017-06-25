class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 0 :
            i -= 1
            if nums[i]< nums[i+1]:
                max2num = nums[i]
                flag = True
                break

        if i == -1:
            nums.reverse()
        else:
            j = i
            while j <= len(nums)-1:
                j += 1
                if nums[j]<=max2num:
                    
                    nums[i], nums[j-1] = nums[j-1], nums[i]

                    break
                if j == len(nums)-1:
                    nums[i], nums[j] = nums[j], nums[i]

                    break

            nums[i+1:] = reversed(nums[i+1:])
