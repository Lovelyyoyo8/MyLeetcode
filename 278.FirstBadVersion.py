# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n+1

        while start < end:
            mid = start + (end - start)//2
            if isBadVersion(mid):
                end = mid
            else: 
                start = mid + 1
        
        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end
        
        return -1


#In Python3, which is shorter
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # first bad is at or before mid
            else:
                left = mid + 1  # first bad is after mid
        
        return left  # or right, since they are equal
