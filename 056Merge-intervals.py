class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if not intervals:
            return []
        
        intervals.sort(key = lambda x:x.start)
        res.append(intervals[0])
        for keys in intervals[1:]:
            cur = res[-1]
            if keys.start <= cur.end:
                cur.end = max(keys.end,cur.end)
            else:
                res.append(keys)
        return res
