class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # Approach: UnionFind Algorithm using Rank
        # O(n) time

        # Create a parent array
        par = [i for i in range(len(edges) + 1)]
        # Create a list of ranks 
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]

            # while parent is not equal to its on parent
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            # Both parents are equal
            if p1 == p2:
                return False

            # if parents are different then union them based on their rank
            if rank[p1] > rank[p2]:
                # p1 is parent of p2
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                # p2 is parent of p1
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]


