"""
Create a hashmap for the count of the %60 values of all times
For example if we have the times [60,30,90], we will get the hashmap {0:1, 30:2}
Now we will iterate over the keys of this hashmap and find the valid pairs.
If the key is 0 or 60, it forms pairs with itself thus we will take math.comb(freq[k], 2), which is nCk
For other keys, we need to find if 60-k exits in the hashmap, since if k is 20, we need all the values whose % is 40 to be valid
If we find it then we add all combinations which is the cartesian product or freq[k]*freq[60-k]. Delete these keys from the hashmap to avoid going over again

O(n) time. One pass to build freq hashmap and one pass over the keys of the hashmap which will be <= n
O(n) space to store the hashmap
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        freq = {}

        for t in time:
            t %= 60
            if t not in freq:
                freq[t] = 1
            else:
                freq[t] += 1
        
        res = 0
        keys = list(freq.keys())
        for k in keys:
            if k in freq:
                if k == 0 or k == 30:
                    res += math.comb(freq[k], 2)
                else:
                    if 60-k in freq:
                        res += freq[k] * freq[60-k]
                        del freq[60-k]
                        del freq[k]
        
        return res
        