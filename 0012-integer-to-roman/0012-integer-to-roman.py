class Solution:
    def intToRoman(self, num: int) -> str:
        intRoman = {
        "I": 1,
        "IV": 4,   
        "V": 5,
        "IX": 9, 
        "X": 10,
        "XL": 40,
        "L":  50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D":  500,
        "CM": 900,
        "M": 1000
                    }
        
        
        
        output = ""
        
        for key, val in reversed(intRoman.items()):
            while num > 0:
                if val <= num:
                    output += key
                    num -= val
                else:
                    break
        return output
                
        
        
        