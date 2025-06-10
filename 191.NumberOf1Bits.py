class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res

#In Python3, Brian Kernighan’s Algorithm (Efficient)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # removes the lowest set bit
            count += 1
        return count

#
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):  # because it's a 32-bit integer
            count += n & 1    # check if the last bit is 1
            n >>= 1           # right shift n by 1
        return count
