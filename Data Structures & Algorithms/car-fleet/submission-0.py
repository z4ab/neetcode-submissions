class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = [[position[i], speed[i]] for i in range(n)]
        pairs.sort(key=lambda p: p[0], reverse=True) # sort by position desc

        stack = []
        for p, s in pairs:
            t = (target - p) / s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)