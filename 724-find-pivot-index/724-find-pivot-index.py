class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
#         Pseudocode:
# variable for left at 0 and right the sum of the list
# iterate through the list in a loop
# set the right sum mines the element
# then check if left is equal to right, if it is return the index
# if it is not them increase the left count + the element
# if this condition doenst match then return -1

        leftSum, rightSum = 0, sum(nums)
        
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                    return idx
            leftSum += ele
        return -1
        