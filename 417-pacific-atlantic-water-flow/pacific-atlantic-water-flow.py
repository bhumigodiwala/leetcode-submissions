class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 
        # Approach : Using hashset and dfs
        # O(n.m) time Flow water from ocean to the cell in increasing order

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r,c) in visit or r < 0 or c < 0 or r == ROWS or c ==COLS or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Run a dfs pass a visit set and since moving from ocean to cell values should be in increasing order or can be equal so we pass prevHeight variable
        for c in range(COLS):
            # Iterate through the first row adjacent to the pacific ocean
            dfs(0, c, pac, heights[0][c])
            # Iterate through the last row adjacent to the atlantic ocean 
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])


        # Run a dfs pass a visit set and since moving from ocean to cell values should be in increasing order or can be equal so we pass prevHeight variable
        for r in range(ROWS):
            # Iterate through the first row adjacent to the pacific ocean
            dfs(r, 0, pac, heights[r][0])
            # Iterate through the last row adjacent to the atlantic ocean 
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                # If (r,c) present in both sets then water flows to both oceans from that cell
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res