class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Approach: Using a Maxheap
        
        # Python doesnt have a max heap
        # so we implement maxheap using minheap by multiplying every value by -1
        
        stones = [-s for s in stones]
        heapq.heapify(stones) # O(n) time operation
        
        # We should be either left with 1 or 0 stones in the end
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if second > first:
                heapq.heappush(stones, -1 * (second - first))
                # heapq.heappush(stones, first - second))
                
        # if stones is empty then we just append a zero
        stones.append(0)
        return abs(stones[0])
            