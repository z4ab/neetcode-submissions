class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ready = []
        for i, [e, p] in enumerate(tasks):
            heapq.heappush(ready, [e, p, i])
        heapq.heapify(tasks) # sorted by enq time
        q = []
        out = []
        time = 0
        while ready or q:
            while ready and ready[0][0] <= time:
                start, length, i = heapq.heappop(ready)
                heapq.heappush(q, [length, i])
            if q:
                length, i = heapq.heappop(q)
                time += length
                out.append(i)
            else:
                time = ready[0][0]
        return out



