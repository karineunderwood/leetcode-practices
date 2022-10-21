class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        compare = len(searchWord)
        
        for idx, word in enumerate(words):
            if word[0:compare] == searchWord: 
                return idx+1
            
        return -1
        
        