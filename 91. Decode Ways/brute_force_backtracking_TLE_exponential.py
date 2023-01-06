class Solution:
    def numDecodings(self, s: str) -> int:

        count = [0]
        
        def backtrack(combo, idx):
            if len(''.join(combo)) == len(s):
                count[0] += 1
                return
            
            if s[idx] != '0' :
                
                # add single char
                combo.append(s[idx])
                backtrack(combo, idx+1)
                combo.pop()
                
                # add 2 chars
                if idx<len(s)-1:
                    if int(s[idx:idx+2]) <= 26:
                        combo.append(s[idx:idx+2])
                        backtrack(combo, idx+2)
                        combo.pop()
        
        backtrack([],0)
        return count[0]
