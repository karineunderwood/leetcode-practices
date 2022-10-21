class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        print(words)
        compare = len(searchWord)
        counter = 0
        
        for idx, word in enumerate(words):
            print(word)
            if word[0:compare] == searchWord: 
                return idx+1
            
        return -1
        
        