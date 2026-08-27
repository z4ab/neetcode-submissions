class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        high = 0

        while l >= 0 and r < n and l < r:
            a = (r - l) * min(heights[l], heights[r])
            high = max(high, a)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return high