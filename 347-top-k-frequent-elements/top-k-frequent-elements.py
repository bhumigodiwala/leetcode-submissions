class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a hashmap with the coutn of every no in list
        counter = {}
        for no in nums:
            if no not in counter:
                counter[no] = nums.count(no)
        
        # Approach 1 using Heap
        # O(Nlogk) time

        # build heap of top k frequent elements and
        # convert it into an output array

        # return heapq.nlargest(k, counter.keys(), key=counter.get)

        # Approach 2 using Bucket Sort Algorithm
        # O(n) time

        # Create an input array same size as that of nums
        # index is the count of an ele and value is the list of elements with that count

        freq = [[] for i in range(len(nums) + 1)]

        for n,c in counter.items():
            freq[c].append(n) # Means n occurs c times

        res = []
        # Iterate in descending order coz finding k most freq ele
        for i in range(len(freq)-1, 0, -1):
            # freq[i] is a list of numbers occuring i times
            for n in freq[i]:
                res.append(n)
                # Code will stop when len of res is equal to k
                if len(res) == k:
                    return res