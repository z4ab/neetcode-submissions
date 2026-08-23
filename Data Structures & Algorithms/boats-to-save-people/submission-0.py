class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0
        r = n - 1

        b = 0
        while l <= r:
            rem = limit - people[r]
            r -= 1
            b += 1
            if l <= r and rem >= people[l]:
                l += 1
        return b