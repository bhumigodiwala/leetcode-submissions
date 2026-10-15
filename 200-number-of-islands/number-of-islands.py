import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque() 
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [(1,0), (0,1), (-1,0), (0,-1)]

                for dr, dc in directions:
                    neigbor_r = row + dr
                    neigbor_c = col + dc

                    if (neigbor_r >= 0 and neigbor_r < rows and neigbor_c >= 0 and neigbor_c < cols
                    and grid[neigbor_r][neigbor_c] == "1" and (neigbor_r, neigbor_c) not in visit 
                    ):
                        q.append((neigbor_r, neigbor_c))
                        visit.add((neigbor_r, neigbor_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

        