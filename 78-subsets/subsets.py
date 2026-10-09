class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Create a result array and the subset array
        res = []
        subset = []

        # Define a recursive function to perform backtracking
        # i -> index of eleements in the nums list
        def dfs(i):
            if i >= len(nums):
                # We completed visiting all elements so we append every subset to the result array
                # Indicates we have reached past the leaf node
                res.append(subset.copy())
                # We add copy of subset because we know it is going to be modified at every call of dfs(i)
                return

            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # Decision NOT to include nums[i]
            # We pop the element added fromthe last call to the dfs at line 18
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res