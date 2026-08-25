class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0] * len(temperatures)
        s = [] # index, temp
        for i, t in enumerate(temperatures):
            while s and s[-1]:
                if t > s[-1][1]:
                    ri, rx = s.pop()
                    r[ri] = i - ri
                else:
                    break
            s.append([i, t])
        return r