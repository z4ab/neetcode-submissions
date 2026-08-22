class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        table = {}
        for i in range(n):
            if nums[i] in table:
                return [table[nums[i]], i]
            table[target-nums[i]] = i
