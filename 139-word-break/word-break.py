class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Initialize the cache with False for all values in s
        dp = [False] * (len(s) + 1)
        # WHen cache reaches end of string the value is True
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            # for each position i try every single position in dict
            for w in wordDict:
                # if i + len(w) is still within len(s) and also check if this word is in word dict
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
