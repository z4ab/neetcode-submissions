class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()

        for newInterval in intervals:
            if not res or res[-1][1] < newInterval[0]:
                res.append(newInterval)
                continue
            else:
                res[-1][1] = max(res[-1][1], newInterval[1])
        return res
