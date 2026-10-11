class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1:Use maxHeap
        # O(klogn) time
        
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
    
        # Approach 2: using maxheap
        # O(klogn) time
        
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap,-num)
        # while k > 0:
        #     res = heapq.heappop(heap)
        #     k -=1
        # return -res
        
        # Approach 3: Brute Force Solution
        # O(nlogn) time
        
        # nums.sort()
        # return nums[len(nums) - k]
        
        # Approach 4: Quick Select Algorithm
        # O(n) avg time complexity and O(n^2) worst time

        # Let k be the indexx that we are looking for 
        # it will give us the k larget element
        
#         k = len(nums) - k
        
#         def quickselect(l,r):
#             pivot, p = nums[r], l
            
#             for i in range(l,r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
            
#             # nums[r] -> pivot element
#             # Swap element at pointer p with the pivot element
#             nums[p], nums[r] = nums[r], nums[p]
            
#             if p > k:
#                 # Run quickselect on left portion of array
#                 return quickselect(l, p - 1)
#             elif p < k:
#                 return quickselect(p + 1, r)
#             else:
#                 return nums[p]
            
#         return quickselect(0,len(nums) - 1)
            
        
        