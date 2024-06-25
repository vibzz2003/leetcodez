class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 

        row, col = len(matrix), len(matrix[0])
        first_row_has0 = False
        first_col_has0 = False

        #checking if the first row has any 0
        for j in range(col):
            if matrix[0][j]==0:
                first_row_has0=True
                break
        
        #checking if the first col has any 0
        for i in range(row):
            if matrix[i][0]==0:
                first_col_has0=True
                break
        
        #using the first row and col as markers to identify the 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        #setting element to 0 on the basis of markers            
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        if first_row_has0:
            for j in range(col):
                matrix[0][j]=0
        
        if first_col_has0:
            for i in range(row):
                matrix[i][0]=0
        