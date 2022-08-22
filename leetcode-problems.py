"""1- Two Sum (Array, int)
Given an array of integers nums and an integer target, 
return indices of the two number such that add up to target.
Return the answer in any order.

Example 1 :
Input: nums =  [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]


"""

# Brute force solution I would check every pair and see if they are equal
# to the target. 
# Time: n*n --> O(n^2)

# More Optimal solution:
# Have a hashmap to keep track of the val and index. Initialize an empty hashmap.
# To get to the sum I can subtract the current number to the target
#      0  1   2    3
# e.g [2, 7, 11, 15], 9 do: (target) 9 - 2 (1st item in the list) = 7
# so the number that I need to to find to sum to 9 is 7. 
# I will check if num - target is in the hash. If it's not then add val as
# a key and index as a value
# keep looping. As soon as you do the check for target - num if the result
# is in the had, then it means that you found the second num (the pair)
# so return [value(index), and the num(index) you just checked]


def two_sum(nums, target):

    tracker = {}

    for idx, num in enumerate(nums):
        difference = target - num
        if difference in tracker:
            return [tracker[difference], idx]
        else:
            tracker[num] = idx
    return 
print(two_sum([2, 7, 11, 15], 9))
