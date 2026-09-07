class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # minheap
        while len(nums) > k: 
            # pop smallest elements until size is k
            heapq.heappop(nums)
        
        # return smallest element after popping
        return heapq.heappop(nums)