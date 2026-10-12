import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Approach: BFS
        # O(m.n) time and memory

        # Initialize the queue with rotten oranges
        q = collections.deque()
        # Keep track of fresh oranges and the time
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If grid cell is 1 then incremment the no of fresh orange
                if grid[r][c] == 1:
                    fresh += 1
                # If grid cell-> 2 means rotten orange so append it to the queue
                if grid[r][c] == 2:
                    q.append((r, c))

        # We move in 4 directions top bottom left and right
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # Do BFS only if the queue is not empty and the no of fresh oranges is greater than 0 
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                # Pop from beginning of the queue the rotten orange co-ordinates
                r, c = q.popleft()
                # Check in all 4 directions
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1