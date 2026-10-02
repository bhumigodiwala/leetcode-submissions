class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1: Hashmap
        # O(n) time and space i.e O(s+t)
        
        # Firstly check if len of both is same else it is false
        if len(s) != len(t):
            return False
        
        # Create a hastable
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Iterate through hashmap
        for c in countS:
            # countT.get(c,0) -> if c doesnt exist in T
            if countS[c] != countT.get(c,0):
                return False
        return True
    
        # Approach 2: Counter 
        # O(n) time and space
        return Counter(s) == Counter(t)
        
        # Approach 3: Sorting
        # O(n^2) to O(nlogn) time and O(1) space
        s = sorted(s)
        t = sorted(t)
        
        if (s==t):
            return True
        return False
    

    
        