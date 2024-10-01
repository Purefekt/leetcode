"""
Mod and hashmap.
Convert input array to mod of all nums.
Then get the frequency of each number.
Suppose k=6, we will have keys 0,1,2,3,4,5.
Iterate through this hashmap, we need to see if there are exactly as many as key as the needed.
Suppose key = 2, we need 4 to sum to 6. So hashmap[2] == hashmap[6], otherwise it is False.
Special case for 0 and k//2 (only if k is even) since it needs itself.
So hashmap[0] and hashmap[k//2] (for even k) must be an even number as well.

O(n) time to mod array, then get the counts.
O(k) space to store counts of all values upto k since mod.
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        # convert arr to mod of each
        arr = [n%k for n in arr]

        # get freq of each
        freq = collections.defaultdict(int)
        for n in arr:
            freq[n] += 1
        
        # go through this hashmap to check if enough corresponding numbers exists
        # special case for 0 and exactly half of k if k is even
        for key,count in freq.items():
            if key == 0:
                if count % 2 != 0:
                    return False
            elif k % 2 == 0 and key == k//2:
                if count % 2 != 0:
                    return False
            else:
                needed = k - key
                if needed not in freq:
                    return False
                if freq[needed] != count:
                    return False
        
        return True