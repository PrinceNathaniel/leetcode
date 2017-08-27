class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        lists,lists2 = [0]*49, [0]*49
        for x in nums:
            tmp = x//10
            val = x%10
            lists[tmp]=1
            lists2[tmp] = val
        for i in range(4):
            lists[31+i]=max(lists[31+i],lists[41+i*2]+lists[42+i*2])
        for i in range(2):
            lists[21+i] = max(lists[21+i],lists[31+i*2]+lists[32+i*2])
        lists[11]=max(1,lists[21]+lists[22])
        for i in range(len(lists)):
            res+= lists[i]*lists2[i]
        return res
