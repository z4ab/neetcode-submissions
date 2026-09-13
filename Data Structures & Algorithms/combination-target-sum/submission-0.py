class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            # 1. add current item
            cur.append(nums[i])
            dfs(i, total + nums[i])
            # 2. skip current item
            cur.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
