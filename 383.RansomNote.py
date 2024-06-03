class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note_dict = {}
        mg_dict = {}
        for r in ransomNote:
            if r not in note_dict:
                note_dict[r] = 1
            else:
                note_dict[r] += 1
        for m in magazine:
            if m not in mg_dict:
                mg_dict[m] = 1
            else:
                mg_dict[m] +=1
        for ch in ransomNote:
            if ch not in mg_dict or mg_dict[ch] < note_dict[ch]:
                return False
        return True 
