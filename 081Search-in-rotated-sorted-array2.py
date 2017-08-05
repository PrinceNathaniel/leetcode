class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left<= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left]:
                left += 1
            elif (nums[mid]<nums[left] and not  nums[mid] < target <=nums[right]) or (nums[mid]>=nums[left] and nums[left]<=target<nums[mid]):
                right = mid -1
            else:
                left = mid +1
        return False
