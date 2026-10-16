import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Approach 1: Brute Force
        # O(max(p).p) time

        # Consider and check for all values of k in range [1, max(piles)]

        # Approach 2: Using Binary Search
        # O(log(max(p))*p) time Optimal Solution

        # Run a binary search over the range of k to find min k

        # Initialise the left and right pointers from 1 to max val in piles
        # l = 1 because Koko cant eat 0 bananas and 
        # r = max(piles) that is always going to be one of the possible solutions
        
        l, r = 1, max(piles)
        res = r

        # Do binary search over k = [1,2, .... , 11] in case of testcase 1
        while l <= r:
            k = (l+r)//2

            hours = 0
            for p in piles:
                # To round up we use math.ceil function
                # p/k gives hours taken to eat that pile
                # sum of hours taken to eat each pile should be <= h
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(r, k)
                r = k - 1
            else:
                l = k + 1
        return res