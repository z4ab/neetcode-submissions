class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and a < 0 and s[-1] > 0: # while a is colliding
                d = a + s[-1]
                if d > 0:
                    a = 0 # destroyed self
                elif d < 0:
                    s.pop()
                else:
                    a = 0
                    s.pop()
            if a:
                s.append(a)
        return s
