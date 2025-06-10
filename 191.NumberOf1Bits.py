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

#In Python3:
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # removes the lowest set bit
            count += 1
        return count
