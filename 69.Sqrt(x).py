#Use Binary Search:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x  #0 and 2 exception
        
        left, right = 0, x  #the purpose is to get left > right, so return right
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
