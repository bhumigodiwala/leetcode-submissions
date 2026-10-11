class KthLargest:
        
    
    # Approach 1: Brute Force Approach 

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort()
#         return self.nums[-self.k]

    # Approach 2: Min Heap of Size k
    
    def __init__(self, k: int, nums: List[int]):
        # minHeap with k Largest integers
        self.k = k
        self.minHeap = nums
        # Convert the minheaparray to a minheap for sorting property using heapify
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k:
            # pop the min element
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # Edge Case that the heap might be initialised with less thank k elements
        # thus apply the below condition
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            # In min heapp the min element is always stored at the 0th index
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)