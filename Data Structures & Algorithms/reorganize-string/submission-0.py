class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_table = {}
        for c in s:
            freq_table[c] = 1 + freq_table.get(c, 0)
        
        max_heap = [[-count, char] for char, count in freq_table.items()]
        heapq.heapify(max_heap)

        # prev = [x, y]
        # max heap = [x1, y1], [x2, y2]
        prev = None
        out = ""
        while prev or max_heap:
            if prev and not max_heap:
                return ""

            count, char = heapq.heappop(max_heap)
            out += char
            count += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if count != 0:
                prev = [count, char]
        return out
