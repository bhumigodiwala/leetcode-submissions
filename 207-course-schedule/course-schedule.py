class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Approach: DFS
        # O(n.p) time n-> no of nodes p-> no of prereq

        # Create a hashmap to map each course to a pre req list
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet -> all courses along the curr dfs path
        visit = set()

        def dfs(crs):
            # If the course is already in visit -> visiting again means there is LOOP
            if crs in visit:
                return False
            # if course has no pre reqs and they happen to be an empty list
            if preMap[crs] == []:
                return True
            
            # Add the course to the visit set
            visit.add(crs)
            # recursively run dfs on the pre req of that course given by preMap[crs]
            for pre in preMap[crs]:
                # if dfs returns false then return false
                if not dfs(pre):
                    return False

            # remove the visited course from the visit set
            visit.remove(crs)
            # Once all the prereqs of course are visited
            # mark it as an empty set indicating course can be completed
            preMap[crs] = []
            return True

        # Iterate through all the courses in num of courses
        # We loop like this beacuse possibly not always we will have a connected graph
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True