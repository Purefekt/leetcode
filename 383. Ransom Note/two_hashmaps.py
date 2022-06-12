class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # if length of ransomnote is more than magazine, then fail
        if len(ransomNote) > len(magazine):
            return False
        
        # using two hashmaps of counts. All letters of ransomnote must appear in magazine and the count of those letters in ransomnote must be less than or eq to the count of those letters in magazine
        
        # build both counter hashmaps
        hashmap_note = {}
        hashmap_mag = {}
        
        for  c in ransomNote:
            if c not in hashmap_note.keys():
                hashmap_note[c] = 1
            else:
                hashmap_note[c] += 1
        
        for c in magazine:
            if c not in hashmap_mag.keys():
                hashmap_mag[c] = 1
            else:
                hashmap_mag[c] += 1
                
        print(hashmap_note)
        print(hashmap_mag)
        
        # each letter in note must appear in magazine. count of each letter in note must be less than count of that letter in magazine
        for c in hashmap_note.keys():
            # if letter is not in  hashmap note, then false
            if c not in hashmap_mag.keys():
                return False
            # if count of letters in note is more than count in hashmap
            elif hashmap_note[c] > hashmap_mag[c]:
                return False
        
        # if for loop doesnt terminate in false, then the checks passed for all characters in ransomNote
        return True
    