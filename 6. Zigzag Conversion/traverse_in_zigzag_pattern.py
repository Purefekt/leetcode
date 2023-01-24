"""
Initialize an array with emty strings for the number of rows, we will build the rows and save them here
Each zigzag has one vertical edge and a diagnol edge and then a new zigzag starts
If we have n number of rows, for each zigzag, we will go down n times and add them to the rows
Then we go up n-2 times for the diagnal edge of the zigzag and add the chars to the corresponding indexes but in reverse
We repeat this till the index surpasses the last.

O(n) time to go over all chars atleast once
O(n) space to store the number of rows in the array
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        rows = ['' for i in range(numRows)]
        
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i<len(s):
                    rows[j] += s[i]
                i += 1
            for j in range(numRows-2, 0, -1):
                if i<len(s):
                    rows[j] += s[i]
                i += 1
        
        return ''.join(rows)
        