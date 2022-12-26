"""
Works for any set of characters. Encode length of chunks
In encode, for each string, add the length of the string followed by a '#'. So for ['hi','world'], it will be 2#hi5#world
In decode, run a while loop, first get the length of a chunk till the first #, then for the length of the chuck, add the characters to result and repeat

O(n) time for both
O(n) space for both
"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res_string = ''
        for string in strs:
            res_string += str(len(string))
            res_string += '#'
            res_string += string
        
        return res_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        res = []
        i = 0
        length = ''
        while i<len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            else:
                length = int(length)
                i += 1
                res.append(s[i:i+length])
                i += length
                length = ''
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))