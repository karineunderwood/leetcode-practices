class Solution:
    def isPalindrome(self, s: str) -> bool:
#         use two pointers, left and right
#         while left is less than right, check:
#           if s[left] == s[right], if they are, return true, otherwise false

        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            elif s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            
        
            
        