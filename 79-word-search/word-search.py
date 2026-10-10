class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Approach: Recursive backtrack
        # O(n * m * 4^n) time

        ROWS, COLS = len(board), len(board[0])
        # Since we can't revisit any character on the board we use set data structure
        path = set()

        # Create a recursive function with below params:
        # r,c -> curr row column position
        # i -> curr character in the target word that we are looking for
        def dfs(r, c, i):
            # Base case if we reach the last char of word
            if i == len(word):
                return True
            
            # Check additional two conditions:
            # 1. the char in word at i NOT EQUAL to char on board
            # 2. the position we are at (r,c) is already inside the path set indicates we are visiting the same char again
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            res =  (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1))
            path.remove((r,c))
            return res

        # Run through the entire board 
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False