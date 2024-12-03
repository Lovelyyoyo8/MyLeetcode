class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
           for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:
                   return([i,j])

# I feel like I have to do this one anyway.#


For Python 3: 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# It takes 1808ms.


# Hashing Map, only takes less than 22ms:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store the number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
