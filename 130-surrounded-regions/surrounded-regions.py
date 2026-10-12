class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Approach: Reverse thinking method and dfs
        # O(n.m) time
            
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Phase 1: Capture unsurrounded regions (change O -> T) uses dfs

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS -1] or c in [0, COLS -1])):
                    capture(r,c)

        # Phase 2: Capture the surrounded regions using double for loop

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"


        # Phase 3: Uncapture the unsurrounded regions (change T -> O) 

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"






       