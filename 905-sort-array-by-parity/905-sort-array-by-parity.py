class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            if nums[left] % 2 != 0:
                holder = nums[left]
                nums[left] = nums[right]
                nums[right] = holder
                right -= 1
            
            
            
        return nums
        