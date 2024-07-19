class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        count = Counter(s)
        res = 0
        odd_found = False

        for cnt in count.values():
            if cnt % 2 == 0:
                res += cnt
            else:
                res += cnt - 1
                odd_found = True

        if odd_found:
            res += 1

        return res

