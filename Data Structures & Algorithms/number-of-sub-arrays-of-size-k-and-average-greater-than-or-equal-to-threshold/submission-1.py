class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed window: subarray has to be size k
        count = 0

        # initial window is 0 up to k + 1 (size k)
        targetsum = threshold * k
        cursum = sum(arr[:k])
        if cursum >= targetsum:
            count += 1
        for r in range(k, len(arr)):
            cursum += arr[r] - arr[r - k]
            if cursum >= targetsum:
                count += 1
        return count