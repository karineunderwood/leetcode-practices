class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        lookup = {}
        
        
        for  val in s:
            if val not in lookup:
                lookup[val] = 1
            else:
                lookup[val] += 1
                
                
        for char in lookup:
            if lookup[char] == 1:
                return s.index(char)
            
        return -1
        