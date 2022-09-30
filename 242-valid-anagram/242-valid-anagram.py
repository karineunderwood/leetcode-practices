class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         check if the lenght of both strings are the same 
#         have a dict to store the chars
#         compare both dicts to see if they match

        if len(s) != len(t):
            return False
    
        count_s = {}
        count_t = {}
        
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else: 
                count_s[char] = 1
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
        
        if count_s == count_t:
            return True
        else:
            return False