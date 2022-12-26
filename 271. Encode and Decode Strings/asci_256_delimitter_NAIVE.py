"""
Asci 256 delimitter
Since the initial range of characers is 256, in the encoder, create a string of each string in strs with chr(256) character between each
At the decoder, split it across the same delimitter

O(n) time for both encode and decode where n is the number of strings
O(1) space for encode since we update the return var res_string. O(n) for decode since output is array of n strings
"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res_string = ''
        for string in strs:
            res_string += string
            res_string += chr(256)
        
        return res_string[:-1]
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = s.split(chr(256))
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))