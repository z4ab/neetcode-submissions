class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # l is a beginning pointer
        # r is searching for numbers that need to go to beginning:
        l = 0
        for r in range(len(nums)):
            # if odd move to beginning
            if nums[r] % 2 == 0:
                nums[l], nums[r], = nums[r], nums[l]
                l += 1
        return nums

