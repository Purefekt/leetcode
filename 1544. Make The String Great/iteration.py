class Solution:
    def makeGood(self, s: str) -> str:
        
        change = True

        while change:
            change = False

            for i in range(len(s)-1):
                # both are the same char
                if s[i].lower() == s[i+1].lower():
                    # both are not the same case
                    if ord(s[i]) != ord(s[i+1]):
                        s = s[:i] + s[i+2:]
                        change = True
                        break
            
        return s
