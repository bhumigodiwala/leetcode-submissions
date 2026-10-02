class Codec:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        # We do the encoding where we store the length of string with '#' sign before the actual string
        for s in strs:
            res += str(len(s)) + "#" + s  #This gives "4#lint4#code4#love3#you"
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        # write your code here
        res, i = [], 0 # i represts the index of str

        while i < len(s):
            j = i #DEfine a second index starting from i
            #Iterate till we reach the delimiter which will give the length of original string
            while s[j] != "#":
                j += 1
            # Length of string is given as below
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))