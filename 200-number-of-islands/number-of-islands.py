import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1: BFS

        # Return 0 if grid is empty
        if not grid:
            return 0

        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Keep track of the visited nodes
        visit = set()
        # Final number of islands to return
        islands = 0

        # Define a breadth first search
        def bfs(r,c):
            # Queue is normally used for bfs
            q = collections.deque()
            # Add the current row and col to both visited and queue
            visit.add((r,c))
            q.append((r,c))
            
            # While the queue is not empty
            while q:
                # we pop the lastly added row colst from the queue
                row, col = q.popleft() # Changing thisto pop will give dfs solution because it willpop the most recent element added to the queue instead of the first element in the queue
                # But it is a non recursive iterative dfs 
                # Since we can move in four directions from a cell
                # [1, 0] -> right, [-1, 0] -> left, [0, 1] -> top, [0, -1] -> bottom
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
                
                # Iterate the (r,c) in all 4 directions
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check the below conditions:
                    # 1. r and c is in range of rows and cols
                    # 2. if that grid cell is "1" ie island
                    # 3. check if the island grid cell is not already visited

                    if ((r) in range(rows) and 
                        (c) in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        # Iterate through the board and run iteratively bfs algo to count no of islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

        # Approach 2: DFS

        # if not grid or not grid[0]:
        #     return 0

        # islands = 0
        # visit = set()
        # rows, cols = len(grid), len(grid[0])

        # def dfs(r, c):
        #     if (
        #         r not in range(rows)
        #         or c not in range(cols)
        #         or grid[r][c] == "0"
        #         or (r, c) in visit
        #     ):
        #         return

        #     visit.add((r, c))
        #     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visit:
        #             islands += 1
        #             dfs(r, c)
        # return islands

