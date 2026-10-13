class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ready = []
        for i, [enq, proc] in enumerate(tasks):
            heapq.heappush(ready, [enq, proc, i])
        
        q = []
        time = 0
        out = []
        while ready or q:
            # if its time for next thread to enque, add it to q
            while ready and ready[0][0] <= time:
                enq, proc, i = heapq.heappop(ready)
                heapq.heappush(q, (proc, i))
            
            # if q is empty, move time up to next thread start
            if not q:
                time = ready[0][0]
                continue
            
            # pop from q and process it, append to output
            proc, i = heapq.heappop(q)
            time += proc
            out.append(i)
        return out
