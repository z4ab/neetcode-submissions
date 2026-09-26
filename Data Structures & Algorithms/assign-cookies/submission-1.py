class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        gi = 0
        si = 0

        res = 0
        while si < len(s) and gi < len(g):
            # if cookie is good enough
            if s[si] >= g[gi]:
                res += 1
                si += 1
                gi += 1
            else:
                gi += 1
        return res