class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        pre = 0
        for i in range(len(nums)):
            size = len(res)
            for j in range(size):
                if i ==0 or nums[i] !=nums[i-1] or j>= pre:
                    res.append(list(res[j]))
                    res[-1].append(nums[i])
            pre = size

        return res
