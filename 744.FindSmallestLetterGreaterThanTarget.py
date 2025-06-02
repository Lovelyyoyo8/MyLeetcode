from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        
        # Binary search loop
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1  # go right
            else:
                right = mid - 1  # go left

        # After loop, left is the index of the smallest letter > target
        # If not found, wrap around using modulo
        return letters[left % len(letters)]
