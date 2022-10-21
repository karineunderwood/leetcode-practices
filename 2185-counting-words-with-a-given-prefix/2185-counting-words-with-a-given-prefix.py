class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        compare = len(pref)
        counter = 0
        
        for i in words:
            if i[:compare] == pref:
                counter += 1
        return counter
        