class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach 1

        # Remember the below conditions:

        # 1. Only add open bracket if open < n
        # 2. Only add close bracket if close < open
        # 3. Valid IFF open == close == n

        stack = []
        res = []

        # Define a recursive function 
        def backtrack(openN ,closeN):
            # if no of open and close brackets
            # are equal to n mens it is valid parenthesis
            if openN == closeN == n:
                # Since we need to return strings
                res.append("".join(stack))
                return
            # we can add open parenthesis only when 
            # no of open ( is less than n
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            # we can add close parenthesis only when
            # no of closed ) is less than open (
            # case like ()) would be invalid
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN+1)
                stack.pop()
                
        # recursively call it initialising open and closed () to 0
        backtrack(0,0)
        return res
