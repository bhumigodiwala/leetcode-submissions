class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointer solution
        # On(n) time and O(1) space

        l,r = 0, len(s) - 1

        def alphanum(c):
            return ((ord('A') <= ord(c) <= ord('Z')) or
                    (ord('a') <= ord(c) <= ord('z')) or
                    (ord('0') <= ord(c) <= ord('9')))
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not alphanum(s[l]):
                l += 1
            while l < r and not alphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True
                

        # # check if isalphanumeric convert to lower and check if rev = original s
        # s = "".join(char.lower() for char in s if char.isalnum())
        # if s == s[::-1]:
        #     return True
        # return False

