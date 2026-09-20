class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # problem:
        # we dont know which char we want of the substring (example 1)
        # how do we find longest substring?
        count = {}
        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)): 
            # update freq map
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            # update maxfreq so far
            maxf = max(maxf, count[s[r]])

            # window_size = r - l + 1
            # window_size - maxf will give how many chars need to be replaced
            # if # of chars to be replaced is > k, the window is invalid
            while (r - l + 1) - maxf > k:
                # remove from window
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
