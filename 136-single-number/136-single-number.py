class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
#         hash map to keep track of how many times the number appears in the list
#         return the num

        track_single_num = {}
        
        for num in nums:
            if num not in track_single_num:
                track_single_num[num] = 1
            else:
                track_single_num[num] += 1
            
        for key, value in track_single_num.items():
            if value == 1:
                return key
            