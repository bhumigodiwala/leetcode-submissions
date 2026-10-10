class Solution:
    # Approach: Backtracking 
    # O(2^n) time

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Base case if reaached the end of string
            if i >= len(s):
                res.append(part.copy())
                return

            # Iterate thru every char in s
            for j in range(i, len(s)):
                # Check if it is palindrome by passing s[i:j+1] using helper
                if self.isPali(s, i, j):
                    # If palidrome then append it to part sublist
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            return res

        dfs(0)
        return res
            