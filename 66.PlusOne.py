class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one: 
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else: 
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]
        

#My solution: convert the array to num and math +1, then turn it back to array
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    num = int("".join(map(str, digits)))  
    num += 1  # Add one
    return [int(d) for d in str(num)]

#It's simple and readable but not optimal for large numbers due to integer conversion overhead.
