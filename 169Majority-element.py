class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        freq = []
        for x in nums:
            if x not in tmp:
                freq.append(nums.count(x))
                tmp.append(x)
        return tmp[freq.index(max(freq))]
