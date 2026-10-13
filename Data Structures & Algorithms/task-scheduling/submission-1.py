class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # build a counter of the tasks
        freq_table = {}
        for t in tasks:
            freq_table[t] = 1 + freq_table.get(t, 0)
        
        # build a max heap of tasks based on count
        max_heap = [-c for c in freq_table.values()]
        heapq.heapify(max_heap)

        # q up tasks with their count left, and idle time
        q = deque()
        time = 0
        while q or max_heap:
            time += 1
            if not max_heap:
                # we are done, jump to time
                time = q[0][1]
            else:
                # if theres tasks left, add to q
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])
            # if theres a task that needs to run now
            # run it and add remaining count back to heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
