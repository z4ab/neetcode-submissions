class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)
        # binary search to find the latest start position which is before new intervals 
        # start position (the right place to insert)
        target = newInterval[0]
        left, right = 0, n - 1 

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        # after this, left should be the right position

        intervals.insert(left, newInterval)

        output = []
        for interval in intervals:
            if not output or output[-1][1] < interval[0]: 
                # top of list ends before current interval starts
                # no overlap 
                output.append(interval)
            else:
                output[-1][1] = max(interval[1], output[-1][1])
        return output
