class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = [""]
        
        if not digits:
            return []
        
        
        for i in digits:
            temp = []
            for s in lookup[i]:
                for k in output:
                    temp.append(k+s)
            output = temp
        return output
                    
        