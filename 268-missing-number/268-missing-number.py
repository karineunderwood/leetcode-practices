class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
#         get the sum of the list 
# then use a formula n*(n+1) // 2
#  then subtract sum of list - sum of expected list

        expected_num = (len(nums) * (len(nums) + 1)) // 2
        return expected_num - sum(nums)
        