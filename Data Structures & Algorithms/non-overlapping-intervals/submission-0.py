class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        ptr = intervals[0][1] # end of interval
        res = 0
        for start, end in intervals[1:]: # skip first interval
            if start >= ptr:
                # start after end of last interval
                ptr = end
            else: # start before end ptr, meaning overlap
                # keep the interval with the smaller end (greedy)
                res += 1
                ptr = min(ptr, end)
        return res


