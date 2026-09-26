class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want o(n), somehow store old prices/profit
        # we see a number and then store it in hashtable
        # map value => profit
        # if we get a value and then another value thats lower then sell on same day
        # what if we compute differences?
        # -6, 4, -2, 3, -2
        # max profit: 7
        # 1, 1, 1, 1
        # max profit: 4

        s = 0
        for i in range(1, len(prices)):
            d = prices[i] - prices[i-1]
            if d > 0:
                s += d
        return s
