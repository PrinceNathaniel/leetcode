class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m+n)%2 ==1:
            return self.getk(nums1,nums2,(m+n)/2+1)
        else:
            return (self.getk(nums1,nums2,(m+n)/2)+self.getk(nums1,nums2,(m+n)/2+1))*0.5
        
    def getk(self,nums1,nums2,k):
        m,n = len(nums1), len(nums2)
        if m > n:
            return self.getk(nums2, nums1,k)
        left, right = 0,m
        while left < right:
            mid = (left+right)/2
            if 0<=k-1-mid<n and nums1[mid]>=nums2[k-1-mid]:
                right = mid
            else:
                left = mid +1
        in1 = nums1[left-1] if left -1>=0 else float("-inf")
        in2 = nums2[k-1-left] if k-1-left >= 0 else float("-inf")
        return max(in1,in2)
