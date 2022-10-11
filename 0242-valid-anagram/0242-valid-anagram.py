class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         check if the lenght of both strings are the same 
#         have a dict to store the chars
#         compare both dicts to see if they match
        if len(t) != len(s):
            return False
        
        sCount = {}
        tCount = {}
        
        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
            
        if sCount == tCount:
            return True
        else:
            return False