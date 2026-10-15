class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            # Check if its the start of the sequence
            if (n-1) not in nums_set:
                length = 0
                while (n+length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest