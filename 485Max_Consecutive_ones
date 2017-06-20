class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[0]
        tmp = 0
        for i in nums:
            if i == 1:
                tmp +=1
            else:
                res.append(tmp)
                tmp = 0
        res.append(tmp)
        return max(res)
