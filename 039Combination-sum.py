class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        self.combination(candidates, target, [], res)
        return res  
        
    def combination(self,candidates, target, tmp, res):
        sumall = sum(tmp) if tmp else 0
        if sumall > target:
            return
        elif sumall== target:
            res.append(tmp)
            return
        else:
            for index, number in enumerate(candidates):
                self.combination(candidates[index:], target, tmp +[number], res)
