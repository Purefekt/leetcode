class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        first = 0
        second = len(s)//2

        count1 = 0
        count2 = 0

        for i in range(len(s)//2):
            if s[first+i] in vowels:
                count1 += 1
            if s[second+i] in vowels:
                count2 += 1
        
        if count1 == count2:
            return True
        return False
