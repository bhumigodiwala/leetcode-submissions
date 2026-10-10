class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach 1: backtrack
        # O(n*4^n) time

        # Create a hashmap to map digits to chars
        dig2char =  {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}

        res = []
        
        # Create a recursive backtracking call
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # Iterate through every char present in strings 'abc' and 'def' as eg 
            # coz 2 -> abc and 3 -> def
            for c in (dig2char[digits[i]]):
                backtrack(i+1, curStr + c)

        if digits:
            backtrack(0, "")
        return res