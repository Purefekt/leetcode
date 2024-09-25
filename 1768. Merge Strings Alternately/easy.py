class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        m = 0
        n = 0

        while m<len(word1) and n<len(word2):
            res.append(word1[m])
            res.append(word2[n])
            m += 1
            n += 1
        
        for i in range(m, len(word1)):
            res.append(word1[i])
        for i in range(n, len(word2)):
            res.append(word2[i])
        
        return ''.join(res)
            