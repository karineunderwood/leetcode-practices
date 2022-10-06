class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = ""
        
        for i in range(len(s)):
            if i != len(s) - 1:
                result += s[i][::-1] + " "
            else:
                result += s[i][::-1]
        return result
                    
                
        