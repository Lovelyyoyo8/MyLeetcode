#In Python:
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


#In Python 3:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n_dict = {}
        m_dict = {}

        for r in ransomNote: 
            if r in n_dict:
                n_dict[r] += 1
            else: 
                n_dict[r] = 1

        for m in magazine:
            if m not in m_dict:
                m_dict[m] = 1
            else:
                m_dict[m] += 1
                
        for ch in ransonNote:
            if ch not in m_dict or m_dict[ch] < n_dict[ch]:
                return False
 
        return True
