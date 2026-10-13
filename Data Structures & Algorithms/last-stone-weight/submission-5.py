class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # need max heap, so negate all values
        # need to work with negative values
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y: # if heaviest is heavier than second
                heapq.heappush(stones, x - y)
                # diff is still negative because x < y
        return abs(stones[0]) if stones else 0
