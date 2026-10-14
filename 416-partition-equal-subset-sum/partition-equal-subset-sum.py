class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Approach: Using DP
        # O(n) time and O(sum(nums)) memory

        # if sum is odd we cant partition ino equal halves
        if sum(nums) % 2:
            return False
        
        # Create a dp set
        dp = set()
        # Add a zero as base case
        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            # go through every changing target value t in the dp set

            # we cant update the dp set while iterating through it
            # so create a newdp set
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
