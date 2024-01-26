"""
Greedy.
A letter can accomodate at most 2 of the other letters on its left.
That is, if we have 'aa', we can break it by adding a 'b'.
But the last letter can accomodate 4 chars. 'aaaa' can be broken with a single 'b' as 'aabaa'.
Thus the element with the lower count can accomodate 2 chars per each and the last one can do 4.
For example, 'aabaabaabaabaa', here the first 3 b's accomodate 2 a's each and the last one does 4.
Create a hashmap of size of the lesser of a or b. Then loop till min(b, (2*a)) and increment each index by 1.
At max our hashmap will have the size of smaller and each will have a value of 2.
Use another variable extra which is b - 2*a, to keep track of any extra chars needed to be added at end.
Now iterate the hashmap, for each index of the small char, we know how many more chars we need to add first.
Thus add the value of hashmap for that key number of large chars to the res, then add a single of the small char to the res.
At the end, append any extra large chars as well, it will be at most 2.

O(a+b) time.
O(min(a,b)) space
"""

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        char_less = 'a'
        char_more = 'b'
        
        if a>b:
            a,b = b,a
            char_less = 'b'
            char_more = 'a'
        
        # This hashmap tells how many large are to the left of a small. Each can get at max 2, last one can get 4
        hashmap = {i:0 for i in range(a)}
        idx = 0
        for j in range(min(b, (2*a))):
            hashmap[idx] += 1
            idx += 1
            idx %= a
        
        extra = b - 2*a

        res = ''
        for i in range(a):
            res += char_more * hashmap[i]
            res += char_less
        
        res += char_more * extra

        return res
