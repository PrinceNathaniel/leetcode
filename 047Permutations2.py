class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.comb(nums,[],res)
        return res
    def comb(self,nums,l,res):
        if not nums:
            res.append(l+[])
            return
        for i ,v in enumerate(nums):
            if i > 0 and nums[i-1]==nums[i]:
                continue
            l.append(nums[i])
            self.comb(nums[i+1:]+nums[:i], l, res)
            l.pop()
