class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        compare = len(pref)
        counter = 0
        
        for i in range(len(words)):
            if words[i].startswith(pref):
                counter += 1
        return counter
        