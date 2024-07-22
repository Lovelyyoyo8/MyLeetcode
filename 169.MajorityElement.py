class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maj = 0

        for num in nums:
            if count == 0:
                maj = num
            count += (1 if num == maj else -1)

        return maj
