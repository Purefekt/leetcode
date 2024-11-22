"""
Two rows are equal if they are identical or if they are completely opposite.
Opposite means the positions of all 0s and 1s are exactly flipped.
row1 = [1,1,1,0]
row2 = [0,0,0,1]
We can convert the rows into a pattern which doesnt care about the flips.
We use T and F to represent either of the values.
We set T=0 if the first element of a row is 0. We set T=1 if the first element of a row is 1.
row1 = [T,T,T,F]
row2 = [T,T,T,F].
This way we can count the freq of all patterns and return the max.

O(m*n) time.
O(m*n) space.
"""

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        # create patterns and store the freq
        freq = collections.defaultdict(int)
        for row in matrix:
            t = row[0]
            pattern = []
            for c in row:
                if c == t:
                    pattern.append('T')
                else:
                    pattern.append('F')
            freq[tuple(pattern)] += 1
        
        return max(freq.values())
