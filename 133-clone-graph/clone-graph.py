"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Approach 1: DFS and using hashmap
        # O(n) time (E+V)

        # Create a hashmap to map old nodes to the new nodes
        oldToNew = {}

        def dfs(node):
            # Check if the node is present in the hashmap
            if node in oldToNew:
                return oldToNew[node]

            # Node is not in hashmap so we create a copy of that node
            copy = Node(node.val)
            # Add the copy node to the hashmap
            oldToNew[node] = copy
            # Go through every single neighbours
            for nei in node.neighbors:
                # dfs will return the copy that we re creating 
                # Using the copy take the list of neighbors and append to it the node returned by dfs 
                copy.neighbors.append(dfs(nei))
            return copy
        if node:
            return dfs(node)
        return None

        