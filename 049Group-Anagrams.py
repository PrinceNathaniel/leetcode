class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        maps = {}
        for i,v in enumerate(strs):
            tmp = ''.join(sorted(v))
            if tmp not in maps:
                maps[tmp] = [v]
            else:
                maps[tmp].append(v)
        res = []
        for v in maps.values():
            res += [v]
        return res
