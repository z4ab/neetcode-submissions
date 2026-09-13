class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        output = []
        i = 0 

        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        # now we have all the intervals that end before the new interval starts
        
        # if new interval ends after current interval starts
        while i < n and newInterval[1] >= intervals[i][0]:
            # new interval merges with current interval
            # merging:
            # start is the smallest of the 2
            # end is the largest of the 2
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        output.append(newInterval) # add the merged interval now

        while i < n: # for the intervals that start after new interval ends
            output.append(intervals[i])
            i += 1
            
        return output
