class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] is number of ways to decode string starting at i
        dp = {n: 1} # string starting at n is empty (1 way)
        for i in range(n - 1, -1, -1): 
            if s[i] == "0":
                dp[i] = 0 # cant start at 0
            else:
                dp[i] = dp[i + 1] # decode with one digit
            
            # check if theres another digit (10-19 or 20-26)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        return dp[0]

            
