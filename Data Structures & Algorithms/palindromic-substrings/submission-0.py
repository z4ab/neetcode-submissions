class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        # 2d array of bools (is s[i to j] a palindrome?)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # note for difference of index:
                # 0 means same index, 1 means next to each other
                # 2 means one char in between

                # so, either no space for a palindrome in between
                # or dp[i+1][j-1] answers if theres a palindrome between
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count

