class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
#             edge case: ---> if len(p) > than len(s), return empty list
        if len(p) > len(s):
            return []
        
#         two dicts to store value from s and p
        sCount = {}
        pCount = {}
        
#         iterate over string p and add them to the dict
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
        if sCount ==pCount:
            result = [0]
        else:
            result = []
        
        left = 0
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1
            
            if sCount[s[left]] == 0:
                sCount.pop(s[left])
            left += 1
            if sCount == pCount:
                result.append(left)
        return result
        
            
        
        
                
            
            