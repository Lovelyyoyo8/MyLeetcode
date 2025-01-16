class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}
#hashing map
        
        for c1, c2 in zip(s, t):  #zip function
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2   #exchange
            mapTS[c2] = c1
        return True
