"""
Easy to understand, if overlap, we generate
the new interval, else, we find a place to put
existing interval.

"""


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
        final = []
        n = newInterval
        nc = Interval(s=n.start, e=n.end)
        s = 0
        for i in intervals:
            if i.end >= nc.start and i.start <= nc.end:
                n.start = i.start if i.start < n.start else n.start
                n.end = i.end if i.end > n.end else n.end
            elif i.end < n.start:
                final += [i]
            else:
                final += [n]
                final += intervals[s:]
                n = None
                break
            s += 1
        final.append(n) if n else None
        return final