class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else: 
                return m
        return -1


#In Python3: 
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid  
            elif nums[mid] < target:
                left = mid + 1  
            else:
                right = mid - 1  

        return -1  # Target not found

        
#So this is the template for binary search: 
        left = 0
        right = len(nums) - 1  #two pointer

        while left <= right:
            mid = (left + right) // 2   #from the middle
            if nums[mid] == target:
                return mid  
            elif nums[mid] < target:
                left = mid + 1  #search right side
            else:
                right = mid - 1  #search left side

        return -1  # Target not found


