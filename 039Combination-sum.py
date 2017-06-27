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
#Method 2:
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(res, candidates,0,target,[])
        return res
        
    def dfs(self, res, candidates, tmp, target, l):
        if target == 0 :
            res.append(l)
            return
        for i in range(tmp, len(candidates)):
            if candidates[i] > target:
                return
            self.dfs(res, candidates, i, target-candidates[i], l +[candidates[i]])
