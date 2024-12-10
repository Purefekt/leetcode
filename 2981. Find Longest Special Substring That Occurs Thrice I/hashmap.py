"""
Hashmap.
Get the counts of each substring.
We just need the longest substring with the same chars, we can use that to get counts of each internal substrings.
For aaaa, we get
4* 'a'
3* 'aa'
2* 'aaa'
1* 'aaaa'
After getting the counts, go through them and get the largest size of a valid substring aka must appear atleast 3 times.

O(n^2) time since we do a loop over all chars, for each substring, we iterate over its size to get the frequency of all its substrings.
O(n^2) space used by all substrings counts.
"""

class Solution:
    def maximumLength(self, s: str) -> int:
        
        counts = collections.defaultdict(int)

        cur_char = None
        cur_size = 0
        for c in s:
            if c != cur_char:
                if cur_char:
                    freq = cur_size
                    for i in range(1, cur_size+1):
                        counts[cur_char*i] += freq
                        freq -= 1
                
                cur_char = c
                cur_size = 1
            else:
                cur_size += 1
        
        # add last substring as well
        if cur_char:
            freq = cur_size
            for i in range(1, cur_size+1):
                counts[cur_char*i] += freq
                freq -= 1
        
        res = -1
        for ss, count in counts.items():
            if count >= 3:
                res = max(res, len(ss))
            
        return res
