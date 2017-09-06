class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        resmax=[0]*n
        resmin = [0]*n
        resmax[0]=resmin[0] = nums[0]
        for i in range(1,n):
            resmax[i] = max(resmax[i-1]*nums[i],resmin[i-1]*nums[i],nums[i])
            resmin[i] = min(resmax[i-1]*nums[i],resmin[i-1]*nums[i],nums[i])
        return max(resmax)
