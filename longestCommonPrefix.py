# Write a function to find the longest common prefix string 
# amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
# initialize the variable for result
    result = ""
    # iterate one element in the list and compare to the nexts:
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result
print(longestCommonPrefix(["flower","flow","floor"]))
    



