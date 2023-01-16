class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in anagramDict:
                anagramDict[sorted_string] = []
            
            anagramDict[sorted_string].append(string)
        return anagramDict.values()


        
        
        
            
            