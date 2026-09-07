class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)
        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            heapq.heappush(min_heap, [d, p[0], p[1]])
        
        output = []
        while k > 0:
            d, x, y = heapq.heappop(min_heap)
            output.append([x, y])
            k -= 1
        return output