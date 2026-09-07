class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            if t in freq:
                freq[t] += 1
            else:
                freq[t] = 1
        
        maxheap = [-f for f in freq.values()]
        heapq.heapify(maxheap)
        cycles = 0
        q = deque() # -count, idletime
        while maxheap or q:
            cycles += 1

            if maxheap:
                count = 1 + heapq.heappop(maxheap) # decrease count by one (negative)
                if count:
                    q.append([count, cycles + n]) # cooldown is current time + wait time
            else:
                cycles = q[0][1]
            # if cooldown is up for top element in q, add it back
            if q and q[0][1] == cycles:
                heapq.heappush(maxheap, q.popleft()[0])
        return cycles
