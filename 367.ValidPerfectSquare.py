class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search range: from 1 to num
        left, right = 1, num
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == num:
                return True  # Found perfect square
            elif square < num:
                left = mid + 1  # Move right to find bigger square
            else:
                right = mid - 1  # Move left to find smaller square
                
        return False  # No perfect square found
