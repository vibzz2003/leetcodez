class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        #check karne padhenge edge cases
        row = len(board)
        col = len(board[0])

        def countliveneighbors(r,c):
            directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            count = 0
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<= nr <row and 0 <=nc<col and (board[nr][nc]==1 or board[nr][nc]==2):
                    count+=1
            return count

        for r in range(row):
            for c in range(col):
                liveneighbors = countliveneighbors(r,c)

                if board[r][c]==1:
                    if liveneighbors<2 or liveneighbors>3:
                        board[r][c]=2
                else:
                    if liveneighbors==3:
                        board[r][c]=3

        for r in range(row):
            for c in range(col):
                if board[r][c]==2:
                    board[r][c]=0
                elif board[r][c]==3:
                    board[r][c]=1
        