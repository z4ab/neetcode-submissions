class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = [sorted(s) for s in strs]

        table = {}
        for s in strs:
            key = str(sorted(s))
            if key in table:
                table[key].append(s)
            else:
                table[key] = [s]
        return list(table.values())
