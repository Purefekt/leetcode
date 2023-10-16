"""
Two words with the same starting letter can never be valid since they will lead to their own word which already exists.
So we can group all words based on their starting letter. This hashmap will be of size O(26) since all are lowercase english chars.
Now we can find the pairs by cartesian product between all these 26 groups.
But there is another condition, for example coffee and toffee are invalid, since they lead to toffee and coffee which already exists.
To avoid this, we need to also not include the pairs which share a suffix.
Use sets intersection for this.

O(n) time to create the hashmap. The nested loop takes constant time since we can have at max 26 keys.
O(m) space if m is the avg size of a word. This is the length of a value set in the hashmap 
"""

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        # create hashmap of first letter to suffixes 
        hashmap = collections.defaultdict(set)
        for s in ideas:
            hashmap[s[0]].add(s[1:])
        
        starts = list(hashmap.keys())
        res = 0
        for i in range(len(starts)):
            for j in range(i+1, len(starts)):
                common = hashmap[starts[i]].intersection(hashmap[starts[j]])
                rem_len_i = len(hashmap[starts[i]]) - len(common)
                rem_len_j = len(hashmap[starts[j]]) - len(common)
                res += (2 * rem_len_i * rem_len_j)
        
        return res
