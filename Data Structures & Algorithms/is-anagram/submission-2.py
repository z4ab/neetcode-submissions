class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        # build freq table based on s
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        # check if freq table matches with string t
        print(table)
        for c in t:
            if c in table:
                table[c] -= 1
                if table[c] == 0:
                    del table[c]
            else:
                return False
        return table == {}
