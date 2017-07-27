class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.comb(nums,[],res)
        return res
    def comb(self,nums,l,res):
        if not nums:
            res.append(l+[])
            return
        for i ,v in enumerate(nums):
            l.append(nums[i])
            self.comb(nums[i+1:]+nums[:i], l, res)
            l.pop()
            
        #method 2
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return nums and [p[i:]+[nums[0]]+p[:i] for p in self.permute(nums[1:]) for i in range(len(nums))] or [[]]
