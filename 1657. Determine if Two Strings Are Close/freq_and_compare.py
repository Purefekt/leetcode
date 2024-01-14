"""
If lengths of both words are different, return False.
Get the frequencies of chars in both words in 2 hashmaps.
The set of unique chars in both words must be the same.
AND the tuple of values of all kv pairs must also be same.
For this, sort the values.

O(1) time since there will be at max 26 keys in the hashmap, thus the lists of keys and values will be of size 26.
O(1) space for the same reason.
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        freq1 = collections.defaultdict(int)
        freq2 = collections.defaultdict(int)

        for i in range(len(word1)):
            freq1[word1[i]] += 1
            freq2[word2[i]] += 1
        
        chars1 = sorted(freq1.keys())
        chars2 = sorted(freq2.keys())

        vals1 = sorted(freq1.values())
        vals2 = sorted(freq2.values())

        return (chars1 == chars2) and (vals1 == vals2)
