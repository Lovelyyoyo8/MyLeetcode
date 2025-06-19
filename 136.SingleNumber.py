from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0  # Start with 0 since a ^ 0 = a
        for num in nums:
            result ^= num  # XOR each number
        return result

