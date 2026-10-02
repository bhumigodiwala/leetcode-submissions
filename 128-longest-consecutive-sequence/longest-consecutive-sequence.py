class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) time and O(n) space

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
        
        # O(nlogn) time
        # if not nums:
        #     return 0

        # nums.sort()

        # longest = 1
        # current = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     elif nums[i] == nums[i - 1] + 1:
        #         current += 1
        #     else:
        #         longest = max(longest, current)
        #         current = 1

        # return max(longest, current)