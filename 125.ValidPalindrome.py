class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        
#In Python3:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())  # Remove non-alphanumeric and convert to lowercase, this is so long that I won't think about it
        return s == s[::-1]  # Check if it reads the same forward and backward


#So here is a more beginner version, which is longer.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []  
        for c in s:  # Step 1: Process each character
            if c.isalnum():  
                cleaned.append(c.lower())  # Step 2: Convert to lowercase and store
            
        cleaned_str = ''.join(cleaned)  # Step 3: Join into a string
        return cleaned_str == cleaned_str[::-1]  # Step 4: Check palindrome
