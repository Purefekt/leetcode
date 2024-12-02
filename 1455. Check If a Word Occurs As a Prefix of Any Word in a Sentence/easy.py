class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        def check(word):
            if len(word) < len(searchWord):
                return False
            word = word[:len(searchWord)]
            if word == searchWord:
                return True
            return False

        sentence = sentence.split(' ')
        for i,word in enumerate(sentence):
            if check(word) is True:
                return i+1
        return -1
