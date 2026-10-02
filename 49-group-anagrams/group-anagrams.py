class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1 
        # O(m*nlogn)

        # Create a dictionary with sorted strs as keys and
        # their corresponding str in original list as values
        # for eg: str[aet] : ['ate', 'eat', 'tea']
        # str_dict = {}
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))

        #     if sorted_s not in str_dict:
        #         str_dict[sorted_s] = []
        #     str_dict[sorted_s].append(s)

        # # Return only the values from the dict as a list
        # res = list(str_dict.values())
        # return res
        
        # Approach 2 (Optimal Solution) 
        # O(m*n) m-> no of strings given n->abg length of each given string

        # Mapping char count of each string to list of Anagrams
        res = defaultdict(list) 

        for s in strs:
            # Initialise count of each character as 0 for 26 chars from a-z
            count = [0] * 26 # a .. z

            # Go through every single char in string and count the char
            for c in s:
                # We want to map a to index 0 and z to 25
                # for this mapping we subtract the ascii value of lowercase 'a'
                # from the ascii value of current char 
                
                count[ord(c) - ord("a")] += 1

            # Since lists cannot be keys we convert count list to tuple
            res[tuple(count)].append(s) 

        return list(res.values())