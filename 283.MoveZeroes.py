from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeros in the list to the end while maintaining the order of non-zero elements.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero = 0

        # Move all non-zero elements to the beginning of the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
