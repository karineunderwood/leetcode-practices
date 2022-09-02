# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in 
# left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#  Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Pseudocode
 # reverse the list to start from the last index
    # then I'll have the carry one var + index variable to keep track in 
    # my while loop
    # while the carry number exists
    # I'll check if the index is equal to 9. If it is the nine will become 0
    # don't forget to increment the index so it terminates de while loop
    # if the index is diff from 9. 
    # just increment 1 to the index -> 8 + 1 = 9
    # after this append 1 to the list 
    # set the carry to 0 so it terminates de while
    # return the list output. As it was reversed to iterate, then reverse again 
    # if the correct output

def plusOne(digits):
    digits = digits[::-1]
    carry_one = 1
    i = 0

    while carry_one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry_one = 0
        else:
            digits.append(1)
            carry_one = 0
        i += 1
    return digits[::-1]

print(plusOne([9,9,9,9]))
            
   

