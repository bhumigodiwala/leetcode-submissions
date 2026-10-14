class Solution:
    def numDecodings(self, s: str) -> int:
        # Approach 1: Recursive cache
        # O(n) time and O(n) memory

        # Initialize the total len of string as 1
        dp = {len(s) : 1}

        # Write a recursive function
        def dfs(i):
            # Base Case -> If i is cached or it is end of string return dp[i]
            if i in dp:
                return dp[i]
            # Base Case -> If the string is starting with 0 means invalid 
            if s[i] == "0":
                return 0
            # String is b/w 1-9 do dfs on subproblem
            res = dfs(i+1)
            if (i + 1 < len(s) and 
                (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")): # makes it a double digit value
                res += dfs(i+2)
            # Caching it
            dp[i] = res
            return res
        return dfs(0)

        # Approach 2: DP Bottom Up Approach
        # O(n) time and O(1) memory

        # Iterating the string in reverse order and rest logic is same

        dp = {len(s) : 1}
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1 < len(s) and 
                (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")): # makes it a double digit value
                dp[i] += dp[i + 2]
        return dp[0]
            
            
