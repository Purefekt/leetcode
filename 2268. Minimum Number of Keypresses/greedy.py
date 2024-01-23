"""
Greedy.
The char with highest frequency must be set to the start of any number on the keypad.
Thus set the top 9 highest freq chars to the start of the 9 keys.
Then the next 9 highest to the 2nd position and the next 8 to the 3rd position.
Create frequency hashmap and then create a list with it and sort it with the frequency. 
Each tuple is (count, char).
Iterate through this, add (i//9 + 1) * list[i][0].
i//9 + 1 is the number of times a key has to be pressed and list[i][0] is the frequency.

O(nlogn) time to sort.
O(n) space for sort and the frequency hashmap and list.
"""

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        
        freq_list = []
        for k,v in freq.items():
            freq_list.append((v,k))
        
        freq_list.sort(reverse = True)

        res = 0
        for i in range(len(freq_list)):
            res += (i//9 + 1) * freq_list[i][0]
        
        return res
