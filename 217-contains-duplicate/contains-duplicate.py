class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A1: Using set
        # O(n) time and O(n) space
        
        unique = set(nums)
        if len(unique) != len(nums):
            return True
        return False
    
        # A2: using hashset
        # O(n) time and O(n) space
        
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        