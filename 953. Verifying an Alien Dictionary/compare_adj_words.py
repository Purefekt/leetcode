"""
Compare adjacent words.
Make sure to check for special case when [aaa, aa] is False.

O(m*n) time where n is the number of words and m is the avg size of a word.
O(1) space since hashmap has O(26) chars.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # give positions to words in order for quick lookup
        positions = {}
        for i,c in enumerate(order):
            positions[c] = i
        
        # compare all adj words to verify order
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            p1 = 0
            p2 = 0

            # verify the first different char 
            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] != word2[p2]:
                    pos1 = positions[word1[p1]]
                    pos2 = positions[word2[p2]]
                    if pos1 > pos2:
                        return False
                    break
                p1 += 1
                p2 += 1
            
            # check for case like: [aaa, aa]
            if p1 < len(word1) and p2 == len(word2):
                return False
        
        return True
            