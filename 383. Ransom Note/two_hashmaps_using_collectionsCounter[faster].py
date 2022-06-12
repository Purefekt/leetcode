class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # obvious fail case
        if len(ransomNote) > len(magazine):
            return False
        
        # create counter hashmaps using collections.Counter datatype
        note_counter = collections.Counter(ransomNote)
        magazine_counter = collections.Counter(magazine)
        
        # All letters in note must be in magazine. The count of those letters in notes must be less than or eq to count of those letters in magazine
        for c in note_counter.keys():
            if c not in magazine_counter.keys():
                return False
            elif note_counter[c] > magazine_counter[c]:
                return False
        
        return True
    