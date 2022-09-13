class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         if length of t is smaller than s, return false
#   iterate over first string 

        char_s = 0
        char_t = 0
        len_s = len(s)
        len_t = len(t)
        
        while char_s < len_s and char_t < len_t:
            if s[char_s] == t[char_t]:
                char_s += 1
            char_t += 1
        if char_s == len(s):
            return True
            
        else:
            return False
        