class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        replace = True
        while replace:
            start_length = len(s)
            for inner in ["{}", "()", "[]"]:
                s = s.replace(inner, "")
            if start_length == len(s):
                replace = False
       
        return s == ""

#in Python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack
