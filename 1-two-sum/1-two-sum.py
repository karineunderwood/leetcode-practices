class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        
#     use a dict to store key and value
        two_sum_dict = {}
        
        for idx, number in enumerate(nums):
            if (target - number) in two_sum_dict:
                return [two_sum_dict[target-number], idx]
            else:
                two_sum_dict[number] = idx
        return []
                
        
        