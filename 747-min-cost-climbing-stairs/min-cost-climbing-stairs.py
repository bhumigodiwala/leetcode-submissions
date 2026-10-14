class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach: Using DP
        # O(n) time and O(1) memory

        # Eg:- [10,15,20] 0 (top)
        cost.append(0)

        # Iterate through the array in reverse order
        # We start with index 3 from backwards i.e cost[-3] = 15
        # because from 20 to top is always going to be 1 jump equal to 20
        for i in range(len(cost) - 3 ,-1, -1):
            # cost[i+1] -> one jump and cost[i+2] -> double jump

            # cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
            cost[i] += min(cost[i+1], cost[i+2])

        # We know cost array is guaranteed to have 2 values
        return min(cost[0], cost[1])