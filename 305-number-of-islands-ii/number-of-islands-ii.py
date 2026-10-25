from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        count = 0
        result = []
        
        # Find with path compression
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        # Union by simple attachment (returns True if merged, False if already in same set)
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        for r, c in positions:
            # Convert 2D coordinate to 1D index
            idx = r * n + c
            
            # Handle duplicate positions in the input
            if idx in parent:
                result.append(count)
                continue
            
            # Add new land
            parent[idx] = idx
            count += 1
            
            # Check 4 adjacent neighbors (up, down, left, right)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                n_idx = nr * n + nc
                
                # If neighbor is within bounds and is also land
                if 0 <= nr < m and 0 <= nc < n and n_idx in parent:
                    # If we successfully union two separate islands, the total count drops by 1
                    if union(idx, n_idx):
                        count -= 1
                        
            result.append(count)
            
        return result