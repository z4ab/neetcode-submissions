class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0 # set unique number
        r = 0 # look for next unique number

        while r < n:
            nums[l] = nums[r]
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1
        return l