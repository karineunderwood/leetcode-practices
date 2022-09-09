class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        soma = 0
        output = []
        for i in nums:
            soma = i + soma
            output.append(soma)
        return output
            
        
#         go through the list of integers.
#         define a new integer
#         variable for output
#         return the new list
     
        
            