class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        names = path.split("/")

        for n in names:
            if not n or n == ".":
                continue
            
            if n == "..":
                if s:
                    s.pop()
            else:
                s.append(n)
        return "/" + "/".join(s)
