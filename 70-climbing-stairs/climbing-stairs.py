class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach: DP Memoization
        # O(n) time
        
        # Create two variables and shift them n-1 times
        one, two = 1, 1

        for i in range(n-1):
            # Store one in the temp variable
            # update one -> one + two
            # update two to original value of one stored in temp
            temp = one
            one = one + two
            two = temp
        return one
        