class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Approach: Using Maxheap and queue
        # O(n * m) time m -> idletime
        
        # Remember:
        # 1.Each task 1 unit time
        # 2.Minimize idle time
        
        # get count of every task(char)
        
        count = Counter(tasks)
        
        # From thehashmap values create a maxheap
        # since python doesnt directly implement maxheap create minheap with values*(-1)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [cnt,idleTime]
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) #Add 1 coz dealing with negatives(maxHeap) or else subtract 1
                if cnt:
                    q.append([cnt, time + n])
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
            