class StockSpanner:

    def __init__(self):
        self.history = []
        

    def next(self, price: int) -> int:
        s = list(self.history)
        r = 1
        while s and s[-1] and price >= s[-1]:
            s.pop()
            r += 1
        self.history.append(price)
        return r

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)