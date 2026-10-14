class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach: Dynamic Programming
        # Tricky Question
        # O(n^2) time

        # Initialize a DP cache as 1 for all elements
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # eg: [1,2,4,3] starting at index i we go over all other values j
            for j in range(i + 1, len(nums)):
                # Apply the condition to update LIS
                # Update LIS only if the array comes to be in increasing order
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

                
        