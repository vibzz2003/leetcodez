class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        row_begin = 0
        row_end = len(matrix)
        col_begin = 0
        col_end = len(matrix[0])
        res = []

        while row_end > row_begin and col_end > col_begin:
            # Traverse the top row
            for i in range(col_begin, col_end):
                res.append(matrix[row_begin][i])
            row_begin += 1
            
            # Traverse the right column
            for j in range(row_begin, row_end):
                res.append(matrix[j][col_end - 1])
            col_end -= 1
            
            if row_begin < row_end:
                # Traverse the bottom row
                for i in range(col_end - 1, col_begin - 1, -1):
                    res.append(matrix[row_end - 1][i])
                row_end -= 1
            
            if col_begin < col_end:
                # Traverse the left column
                for j in range(row_end - 1, row_begin - 1, -1):
                    res.append(matrix[j][col_begin])
                col_begin += 1

        return res


        #for i in range (1st column to 3rd column)
        #append matrix[0][0], m[0][1], m[0][2]
        #for j in range (2nd row to last row):
        #append m[1][2], m[2][2] col_end-1 as col_end = len which is 3 and indexing starts from 0
        #now row_end(2)!=row(begin+1)(1)
        #for i in range (1st column to -1 column):
        #append m[2][1] amd m[2][0]
        #for i in range (row 1 to 0 in decreasing order):
        #append m[1][0]
        #then update the value of row_begin to 1, row_end to 2, col_begin to 1 and col_end to 2
        #and then the loop again