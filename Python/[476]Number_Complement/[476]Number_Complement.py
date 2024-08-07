# Your Python code goes here.
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]

        flipped_binary = "".join(["0" if bit == "1" else "1" for bit in binary])

        if flipped_binary:
            return int(flipped_binary, 2)
        else:
            return 1
