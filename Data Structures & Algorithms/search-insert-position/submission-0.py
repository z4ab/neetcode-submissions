class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        mid = 0
        res = n

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
