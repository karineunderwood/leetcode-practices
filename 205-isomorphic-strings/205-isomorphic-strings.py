class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         have to maps to store the characters from string s and t
#         only one char can map to the other char
#         length of both strings has to be the same 

        map_st = {}
        map_ts = {}
        
        for char in range(len(s)):
            char1 = s[char]
            char2 = t[char]
            
            if char1 in map_st and map_st[char1] != char2:
                return False
            if char2 in map_ts and map_ts[char2] != char1:
                return False
            
            map_st[char1] = char2
            map_ts[char2] = char1
            
        return True
        
        