class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed = set([c for c in allowed])
        res = 0

        def is_allowed(w):
            for c in w:
                if c not in allowed:
                    return False
            return True

        for w in words:
            if is_allowed(w) is True:
                res += 1
        
        return res
        