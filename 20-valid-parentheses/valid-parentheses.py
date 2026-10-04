class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time and O(n) space
        #Create bracket pairs
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        #Since we need to also have brackets in correct order it follows 
        # Last In First Out (LIFO) thus use stack data structure
        stack = []

        for bracket in s:
            # Check if bracket is opening bracket as oer keys in pairs 
            if bracket in pairs:
                #append it to the stack
                stack.append(bracket)
            #If it is a closing bracket then check below
            # cond 1: If stack is empty return False
            # cond 2: if stack is not empty then pop last element of stack and compare
            #         it with the value of key given by the poped element
            #         if matches then it is valid
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
        #Finally check if the length of stack is empty then all brackets are closed so 
        # it is valid parenthesis or else it is invalid
        return len(stack) == 0