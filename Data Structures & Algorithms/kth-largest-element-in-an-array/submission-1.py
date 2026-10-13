class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert nums to min heap
        # remove smallest until k elements left
        # smallest is now kth largest
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]