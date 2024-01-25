class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        mapping = {}
        mapping_round = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False
            if t[i] not in mapping_round:
                mapping_round[t[i]] = s[i]
            else:
                if mapping_round[t[i]] != s[i]:
                    return False
        
        return True
