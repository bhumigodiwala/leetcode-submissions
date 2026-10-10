class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Base Case
        if len(nums) == 1:
            # return [nums.copy()] #Makes execution slower
            return [nums[:]]

        for i in range(len(nums)):
            # nums = [1,2,3]
            # Pop the first value or value at the 0th index
            n = nums.pop(0)
            # Do a recursive call to find perm of the sublist obatined after popping nums(0)
            perms = self.permute(nums)
            # perms of (nums = [2,3]) -> [2,3,1] and [3,2,1]

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            # NOw add the popped element back
            nums.append(n)
        return res