"""
Shift the stones right in each row as much as possible.
Then rotate right which means change each col to row but in opposite order.
[a,b,c]
[d,e,f]
becomes
[d,a]
[e,b]
[f,c]

O(m*n^2) time.
O(m*n) space
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        # shift each stone to the right in the box till it hits a stone or object
        for row in box:
            for i in range(len(row)-1, -1, -1):
                last_empty = i
                if row[i] == '#':
                    for j in range(i+1, len(row)):
                        if row[j] == '.':
                            last_empty = j
                        else:
                            break
                    row[i] = '.'
                    row[last_empty] = '#'

        # rotate
        m = len(box)
        n = len(box[0])
        
        res = []
        for j in range(n):
            row = []
            for i in range(m-1, -1, -1):
                row.append(box[i][j])
            res.append(row)
        
        return res
