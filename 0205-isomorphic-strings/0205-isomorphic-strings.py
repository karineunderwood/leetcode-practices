class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         have to maps to store the characters from string s and t
#         only one char can map to the other char
#         length of both strings has to be the same 

        map_s = {}
        map_t = {}
        
        for char in range(len(s)):
            char1 = s[char]
            char2 = t[char]
            
            if char1 in map_s and map_s[char1] != char2:
                return False
            if char2 in map_t and map_t[char2] != char1:
                return False
            map_s[char1] = char2
            map_t[char2] = char1
        return True
        
        