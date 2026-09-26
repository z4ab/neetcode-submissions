class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        n = len(s)
        l = 0
        # start with tset having all of t
        # expand window (right) and check for s[r] in tset
        # if we match s[r] in t, then remove from tset
        # if tset is empty, the window is valid
        # while tset is empty shrink window from the left
        # keep track of smallest valid window
        tset = {}
        # keep track of chars which we fully have
        have = 0
        # and chars which we dont fully have
        for c in t:
            tset[c] = 1 + tset.get(c, 0)
        need = len(tset)
        minw = None
        res = [0, 0]
        freq = {}
        for r in range(n):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            if s[r] in tset and freq[s[r]] == tset[s[r]]:
                    have += 1
            while have == need:
                curw = r - l + 1
                if not minw or curw < minw: # new winner
                    res = [l, r]
                    minw = curw
                freq[s[l]] -= 1
                if s[l] in tset and freq[s[l]] < tset[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if minw:
            return s[l:r+1]
        else:
            return ""


