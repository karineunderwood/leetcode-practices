class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        
        for num in nums:
            if num in lookup:
                lookup[num] += 1
                if lookup[num] > 1:
                    return True
            else:
                lookup[num] = 1
        
        return False
        
            
            
        