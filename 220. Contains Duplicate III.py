class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t<0:
            return False
        dicts={}
        for i,x in enumerate(nums):
            index = x/(t+1)
            if index in dicts or (index+1 in dicts and abs(dicts[index+1]-x)<=t ) \
                    or (index-1 in dicts and abs(dicts[index-1]-x)<=t) :
                return True
            dicts[index] = x
            if i >=k:
                del dicts[nums[i-k]/(t+1)]
        return False
