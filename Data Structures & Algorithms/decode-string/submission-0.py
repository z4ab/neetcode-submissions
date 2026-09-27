class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        outstack = []
        cur = ""
        k = 0
        for c in s:
            if c == "[":
                outstack.append(cur) 
                st.append(k)
                cur = ""
                k = 0
            elif c == "]":
                old = cur
                cur = outstack.pop()
                count = st.pop()
                cur += old * count
            elif c.isdigit():
                k = k * 10 + int(c) # handle multiple digits
            else:
                cur += c
        return cur