class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxprof = 0
        for r in range(len(prices)):
            p = prices[r] - prices[l]
            if p < 0:
                l = r
            else:
                maxprof = max(p, maxprof)
        return maxprof
            
