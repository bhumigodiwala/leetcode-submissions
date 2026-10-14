class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach: DP

        # rob2 -> last house we robbed rob1 -> house before the adjacent of the robbed house
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ....] If we choose rob2 then we cant add n because it is adjacent to rob2
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

