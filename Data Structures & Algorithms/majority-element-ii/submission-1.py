class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        
        out = []
        for k, v in freq.items():
            # n // 3 returns int/floor of result
            if v > n//3: 
                out.append(k)
        return out
