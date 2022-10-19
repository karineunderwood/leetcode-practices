class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        lookupMagazine = {}
        
        for char in magazine:
            if char not in lookupMagazine:
                lookupMagazine[char] = 1
            else:
                lookupMagazine[char] += 1
        
        for char in ransomNote:
            if char not in lookupMagazine:
                return False
            elif char in lookupMagazine and lookupMagazine[char] <= 0:
                return False
            lookupMagazine[char] -= 1
        return True
        