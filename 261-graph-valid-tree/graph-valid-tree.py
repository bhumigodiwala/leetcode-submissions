class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # create adj list
        adj_list = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # define a visit set for tracking cycles
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for j in adj_list[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False # Loop detected
            return True

        return (dfs(0, -1) and len(visit) == n)
            