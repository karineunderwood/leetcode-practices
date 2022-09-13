class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         if length of t is smaller than s, return false
#   have two pointer for char s and char t
#  while char s is less than the len of s and char t is less than len of t
# check if the char from s is equal to char from t
#  if it is then increment char s
#  if its not move the pointer char t to next by increment by one
# when exit the while condition then check if char s is equal to the len of s
# if yes, return true, otherwise, false

        if len(t) < len(s):
            return False
        
        charS = 0 
        charT = 0
        
        while charS < len(s) and charT < len(t):
            if s[charS] == t[charT]:
                charS += 1
            charT += 1
            
        if charS == len(s):
            return True
        return False
        
        
        
    