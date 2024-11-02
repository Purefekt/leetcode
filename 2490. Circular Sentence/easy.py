class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        # append first word to the sentence
        sentence = sentence.split(' ')
        sentence.append(sentence[0])

        # check between all adjacent words
        for i in range(len(sentence)-1):
            if sentence[i][-1] != sentence[i+1][0]:
                return False
        return True
