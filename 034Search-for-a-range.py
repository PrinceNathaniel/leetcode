class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        def binsearch(sign, nums, target):
            left, right = 0, len(nums)-1
            if sign == -1:
                while left <= right:
                    mid = (left +right)/2
                    if nums[mid] >= target:
                        right = mid-1
                    else:
                        left = mid+1
                if left>=len(nums):
                    return -1
                return left
            elif sign == 1:
                while left <= right:
                    mid = (left +right)/2
                    if nums[mid] <= target:
                        left = mid +1
                    else:
                        right = mid -1
                return right
        index1=binsearch(-1,nums,target)
        if nums[index1] != target:
            return [-1, -1]
        index2 = binsearch(1,nums,target)
        return [index1, index2]
