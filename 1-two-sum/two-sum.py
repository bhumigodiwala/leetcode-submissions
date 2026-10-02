class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute force
        # # O(n^2) time and O(1) space
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # using hashmap
        # O(n) time and O(n) space
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            # if dont find solution then need to update hashmap
            # not in hashmap case
            hashmap[n] = i
        return