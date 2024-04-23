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
