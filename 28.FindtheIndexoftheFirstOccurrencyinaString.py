class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

#ChatGPT gives another simpler solution: 
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)
    
