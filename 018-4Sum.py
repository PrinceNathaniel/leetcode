class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def NSum(nums, target, N, preres, res):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return
            if N == 2:
                j, k = 0, len(nums)-1
                while j<k:
                    sum2 = nums[j] + nums[k]
                    if sum2 == target:
                        res.append(preres + [nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j-1]:
                            j+=1
                    elif sum2 < target:
                        j +=1
                    elif sum2 > target:
                        k -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i>0 and nums[i-1]!=nums[i]):
                        NSum(nums[i+1:],target-nums[i],N-1,preres+[nums[i]], res)
        res=[]
        NSum(sorted(nums), target, 4, [], res)
        return res
