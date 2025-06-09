class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

#In Python3:
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            bit = n & 1               # Get the last bit of n
            result = (result << 1) | bit  # Shift result left and add the bit
            n >>= 1                  # Shift n right to process next bit
        return result
