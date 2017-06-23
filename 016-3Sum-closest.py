class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, mdist, i = float("inf"), float("inf"), 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, len(nums) -1
                while j < k:
                    dist = nums[i] +nums[k]+nums[j]-target
                    if abs(dist) < mdist:
                        mdist = abs(dist)
                        res = nums[i] + nums[j] + nums[k]
                    if dist < 0:
                        j += 1
                    elif dist > 0:
                        k -= 1
                    else:
                        return target
            i += 1
        return res
