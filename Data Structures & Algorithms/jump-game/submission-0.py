class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal starts as the end of the list
        goal = len(nums) - 1

        # reverse iterate through previous positions to see if we can get to the goal
        for i in range(len(nums) - 2, -1, -1):
            # if we can get to current goal
            if nums[i] + i >= goal: 
                # new goal is this point
                goal = i
        return goal == 0 # if the final goal is the beginning, then true
