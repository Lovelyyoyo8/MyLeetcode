#My first write it!

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip().split() #got helped by GPT

        if len(s) == 0:
            return 0
        else: 
            count = len(word[-1])
            return count

#ChatGPT use only 1 line, but not consider 0 condition separately, which also work.
def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split()[-1])
