from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Approach 1

        # https://www.youtube.com/watch?v=TjFXEUCMqI8&t=789s

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) #The key for subsquare is (r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                # Check if there is blank space in board
                if board[r][c] == ".":
                    continue
                # Check if the no is in hashset rows whose key is r (rows[r]) 
                # since rows is a set it will check there is no duplicates
                # Similarly check for columns

                # Also check the subsquares condition by checking if the no is present in 
                # the squares hashset which has keys obtained by pair (r/3,c/3)
        
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True