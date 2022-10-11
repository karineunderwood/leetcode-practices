class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        
        for s in strs:
            sortString = "".join(sorted(s))
            
            if sortString not in result:
                result[sortString] = []
                
            result[sortString].append(s)
                
        return result.values()
                
            
            