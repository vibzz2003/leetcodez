class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row ke liye check
        #column ke liye check
        #3X3 ke liye check lagana hoga
        #dict = 1 to 9 
        #ya toh element na ho
        #aur agar ho toh value!>1
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue
                
                #check row
                if num in rows[i]:
                    return False
                rows[i].add(num)

                #check column
                if num in columns[j]:
                    return False
                columns[j].add(num)

                #check for boxes
                box_index = (i//3) * 3 + (j//3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        return True
