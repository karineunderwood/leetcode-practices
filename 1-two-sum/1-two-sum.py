class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        find_target = {}
        
        for idx, num in enumerate(nums):
            if (target - num) in find_target:
                return [find_target[target-num], idx]
            else:
                find_target[num] = idx
                
        return []

        
        

                
        
        