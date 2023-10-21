class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)

        i = 0
        j = 0
        res = 0
        for _ in range(n):
                r = i
                c = n - 1 - j
                
                if (i,j) != (r,c):
                    res += mat[i][j]
                    res += mat[r][c]
                else:
                    res += mat[i][j]

                i += 1
                j += 1

        return res