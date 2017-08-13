class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == 1:
            return arr
        left, right = 0, len(arr)-1
        while left<right:
            mid = (left+right)/2
            if arr[mid]>x:
                right = mid-1
            elif arr[mid]<x:
                left = mid +1
            else:
                left, right = mid,mid

        i = max(0,left-k)
        suml = []
        suml.append(0)
        pre =0
        sum = 0

        while i+k<len(arr) and i<=left:

            
            
            pre =abs(arr[i]-x)

            i +=1
            sum+=abs(arr[i+k-1]-x)-pre
            suml.append(sum)
        res=[]
        i = suml.index(min(suml))+max(0,left-k)
        for m in range(i,i+k):
            res.append(arr[m])
        return res
