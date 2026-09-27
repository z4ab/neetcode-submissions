class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        best = 0
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if sq > x:
                r = mid - 1
            else:
                best = max(mid, best)
                l = mid + 1
        return best
