class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.split("-")
        s = ''.join(s)
        
        new_s = []
        start = len(s)-k
        end = len(s)
        for i in range(len(s)//k):
            new_s.append(s[start:end].upper())
            end = start
            start = start-k
        # add the first group
        if end != 0:
            new_s.append(s[0:end].upper())
        
        s = ""
        while new_s:
            s += new_s.pop()
            s += '-'
        return s[:-1]
        