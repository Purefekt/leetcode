class Solution:
    def sortSentence(self, s: str) -> str:
        
        hashmap = {}
        s = s.split(' ')
        for w in s:
            idx = w[-1]
            word = w[:-1]
            hashmap[int(idx)] = word
        
        res = []
        for i in range(len(hashmap)):
            res.append(hashmap[i+1])
        
        return ' '.join(res)
