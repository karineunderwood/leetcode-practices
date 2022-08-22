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

# Run Time: O(n) -> iterate through the whole string
# Space: O(1) -> did not use an extra memory

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


""" 2 - Roman to Integer (string)
    Given a roman numeral, convert it to an integer.

    Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3

    Example 2: 
    Input: s = "LVIII"
    Output: 58
    Explanation:L = 50 V = 5 III= 3

"""

# start with a hashmap with Symbol as key and value as val.
#  set a variable for result initialy at zero
# check on the iteration if the number we are checking is smaller than 
# the next number, then subtract it from the result 
# if it is larger than add it to the result

def roman_to_integer(s):
    roman_map = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    return result
print(roman_to_integer("MCMXCIV"))


""" 26 - Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element 
appears only once.
The relative order of the elements should be kept the same.
Return k after placing the final result in the first k slots of nums

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

# initialize a counter at 1
# do this iteration until the index is smaller than the length of the list
# iterate through the list and check:
# if the number at the index that I started(index 1) is equal
# to index - 1, that means they are duplicates
# then remove/pop from the list
# if the number is not equal to the number before, then increase the counter/index.
# at the end return the length of the list with the duplicates removed from it

def remove_duplicates(nums):

    counter = 1

    while counter < len(nums):
        if nums[counter] == nums[counter - 1]:
            nums.pop(counter)
        else:
            counter += 1
    return len(nums)
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))


""" 268 - Missing Number (Array)
Given an array nums containing n distinct 
numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""

# Brute force: 
# sort the list using sorted()
# then loop through list and check if the num is different than nums[index]
# if it is then return the num

# Optimal Solution with no extra space 
# we can use a formula sum of list n numbers = n*(n+1)//2
# n is equal to the length of nums - > [0, 1, 2, 3, 5] n = 5
# expected sum will be 5*6 // 2 = 15
# we sum all the numbers in the list sum of nums = 11
# then subtract expected from actual sum 15 - 11 = 4
# the missing number is 4

# Time Complexity : O(n) -> went through the whole list to sum the numbers
# Space: O(1) -> No extra memory

def missing_number(nums):

    expected_num = (len(nums)*(len(nums) + 1)) // 2
    return expected_num - sum(nums)

print(missing_number([9,6,4,2,3,5,7,0,1]))


