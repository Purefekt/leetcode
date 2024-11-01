class Solution:
    def makeFancyString(self, s: str) -> str:
        
        new_str = []
        for c in s:
            if len(new_str) >= 2 and new_str[-1] == new_str[-2] and c == new_str[-1]:
                continue
            else:
                new_str.append(c)
        
        return ''.join(new_str)
