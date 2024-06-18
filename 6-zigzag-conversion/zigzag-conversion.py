class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or not s:
            return s
        
        rows = [''] * numRows #creating list of strings to represent each row in the form of zigzag
        #for eg :  numRows = 3: ["","",""]

        #initialise current row index and sirection of movement
        row_idx, direction = 0, 1

        for char in s:
            rows[row_idx] += char #append the caharavter to the current row

            row_idx += direction #update the current row index based on the direction of movement

            if row_idx==0 or row_idx==numRows-1: #if we reacg the top or bottom then change the direction 
                direction *= -1

            #["p","",""]
            #["p","a",""] 
            #["p","a","y"] now the direction would be -1 after this
            #["p","ap","y"] now it will go to idx 0 and the direction will change
            #["p","apa","y"] same thing, now it willl go to numRows-1 so direction change
            #["p","apal","y"]
            #["p","apali","y"]
            #["p","apalis","y"]
            #["p","apalish","y"]
            #["p","apalishi","y"] ..continue

        return ''.join(rows)

