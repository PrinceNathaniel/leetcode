# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s,e = newInterval.start,newInterval.end
        left = list(filter(lambda x:x.end<s,intervals))
        right = list(filter(lambda x: x.start>e, intervals))
        if len(left)+len(right) != len(intervals):
            s=min(s,intervals[len(left)].start)
            e=max(e,intervals[-len(right)-1].end)
        return left+[Interval(s,e)]+right
