class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        soma = 0
        output = []
        
        for num in nums:
            soma += num
            output.append(soma)
        return output
            
            
        
            