class Solution:
    def removeVowels(self, s: str) -> str:
        
        res = ""
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for c in s:
            if c not in vowels:
                res += c
        
        return res
        