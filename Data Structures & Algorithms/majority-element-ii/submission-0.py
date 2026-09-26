class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        out = set()
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
            # n // 3 returns int/floor of result
            if freq[x] > n//3: 
                out.add(x)
        return list(out)
