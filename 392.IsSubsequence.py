class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

#two pointer, remember i += 1, next line j += 1
