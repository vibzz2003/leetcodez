class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    if all(mat[r][j] == 0 for j in range(cols) if j != c):
                        if all(mat[i][c] == 0 for i in range(rows) if i != r):
                            count +=1
        return count