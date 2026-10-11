class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute Force Approach
        # calculate dist of all points from origin
        # sort the points based on the dist
        # return the k closest points
        
        # Approach: minHeap
        # O(klogn) time
            
        minHeap = []
        for x, y in points:
            # calculate dist from origin
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])
        
        # Convert the list to a minheap
        # this will reorder and transform it to a minheap
        heapq.heapify(minHeap)
        
        res = []
        while k>0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
    
    