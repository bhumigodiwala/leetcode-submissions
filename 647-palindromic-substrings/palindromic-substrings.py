class Solution:
    def countSubstrings(self, s: str) -> int:
        # Appraoch: Use DP
        # O(n^2) time

        # Default palidrome res string count
        res = 0

        # oddLen string case -> Iterate through every position in the string considering it as center
        for i in range(len(s)):
            #odd len string case
            # Use two pointers l and r
            l, r = i, i
            
            # While both pointers are in bounds and it is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even len string case
            l, r = i, i + 1
            
            # While both pointers are in bounds and it is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res