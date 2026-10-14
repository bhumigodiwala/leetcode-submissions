class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach: Different type of DP problem


        # Initialise the result with max value in nums
        res = max(nums)
        # Keep track of current min and max
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                # if we encounter a zero reset the current min and max to 1
                curMin, curMax = 1, 1
                continue
            
            # Calculate the max and min of the below conditions:
            # 1. n * curMax -> curMax and n is +ve
            # 2. n * curMin -> curMin and n is -ve
            # 3. n
            
            # using tmp so that curMax is not overwritten
            tmp = n * curMax 

            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res