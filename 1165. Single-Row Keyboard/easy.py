class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        indexes = {}
        for i,c in enumerate(keyboard):
            indexes[c] = i
        
        res = 0
        cur_pos = 0
        for i in range(len(word)):
            res += abs(cur_pos - indexes[word[i]])
            cur_pos = indexes[word[i]]
        
        return res
