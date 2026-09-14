class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs(numsleft):
            if not numsleft:
                res.append(cur.copy())
                return
            for n in numsleft:
                cur.append(n)
                dfs(numsleft - {n})
                cur.pop()


        dfs(set(nums))
        return res