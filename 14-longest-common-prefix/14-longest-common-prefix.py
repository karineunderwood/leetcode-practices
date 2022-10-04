class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
#     initialize a output variable
#     starts iterating from the first string
#     then check every element in the list
#     if its out of bounce than exits. 
#     if the char at the index from one ele is different from the same index from the next elem, then exits and return empty string
#     otherwith means that they are common then add the i to the output. 
        
        if len(strs) == 1:
            return strs[0]
    
        result = ""
       
    
        for i in range(len(strs[0])):
            for elem in strs:
                if i == len(elem) or elem[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
            
    

                
            
        
        
        
        
        
            
                
                
                
        
        
            
        