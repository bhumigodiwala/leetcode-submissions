class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        freq = [[] for i in range(len(nums)+1)]

        for n,c in counter.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res