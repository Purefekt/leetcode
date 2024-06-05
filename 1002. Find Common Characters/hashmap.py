class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        freq = {}
        for i in range(26):
            freq[chr(ord('a') + i)] = [0 for i in range(len(words))]
        
        for i in range(len(words)):
            for c in words[i]:
                freq[c][i] += 1

        res = []
        for k,v in freq.items():
            if sum(v) >= len(words) and min(v) >= 1:
                for _ in range(min(v)):
                    res.append(k)
        
        return res
