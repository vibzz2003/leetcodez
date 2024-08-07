from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        
        rows,cols = len(board), len(board[0])

        def bfs(r,c):
            queue = deque([(r,c)])
            board[r][c] = "#"
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < rows and 0<= ny < cols and board[nx][ny] == "O":
                        board[nx][ny] = "#"
                        queue.append((nx, ny))
        
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols-1] == "O":
                bfs(r, cols-1)
        
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows-1][c] == "O":
                bfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"