class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Approach: Topological Sort
        # O(E + V) = O(p + n) time p-> no prereq, n-> no of courses

        # build an adjacency list for prereqs using HASHMAP
        preMap = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Course has 3 possible states:
        # visited -> crs has been added to the output
        # visiting -> crs has NOT ADDED to output, but ADDED to CYCLE
        # unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            # if course is in the cycle then false
            if crs in cycle:
                return False
            # if course is already visited return True
            if crs in visit:
                return True

            # Add course to cycle set so that if we revisit we know that its a cycle
            cycle.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False: # indicates we detected a cycle
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output





