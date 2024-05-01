class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        first_occ = None

        for i,c in enumerate(word):
            if c == ch:
                first_occ = i
                break
        
        if not first_occ:
            return word
        
        res = word[:first_occ+1][::-1] + word[first_occ+1:]

        return res
        