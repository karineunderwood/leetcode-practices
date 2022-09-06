class Solution:
    def isPalindrome(self, x: int) -> bool:
#        If it's a negative number it's not a palindrome
        
        
        
        
#         1 - make a backwards copy and compare with the given int
#         2-  how to make the bw copy? the given num mudulo by 10 will give us the last digit. 
#         3 - starts bw copy at 0 and while there's value left for copy multiply by 10 and sum the num % 10
#         to keep track of the given num do num // 10. It will keep the first nums. 
#         4 -  Do it until num reaches to zero and then compare the backwards copy. 
        
        if x < 0:
            return False
        
        
        copy_x = x
        backwards_copy = 0
        
        while copy_x:
            backwards_copy = backwards_copy * 10 + copy_x % 10
            copy_x = copy_x // 10
        
        if backwards_copy == x:
            return True
        else:
            return False
        
        