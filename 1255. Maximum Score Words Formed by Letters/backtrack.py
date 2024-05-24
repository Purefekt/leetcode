"""
Backtracking.
At each level, we need to either keep or skip current word.
We can keep only if we still have enough chars for this word.
Use a function to determine if we can use current word. NOTE: pass a copy of current frequency, since reference will cause issues.
If we decide to keep a word, we add that word's score to it.
If we skip a word, we dont add any score.

O((m+a)*2^n) time where n is the size of words. m is the max length of a word and a is the size of alphabet. The backtrack function has height of n and branching factor of 2. Each call also needs to check if the word is valid which takes m time and score which takes a time.
O(a+w) space since freq and scores maps take a space each since we can have at most a keys. The call stack takes w time.
"""

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        freq = collections.defaultdict(int)
        for c in letters:
            freq[c] += 1
        
        scores = {}
        for c in freq:
            scores[c] = score[ord(c) - ord('a')]

        def can_keep(w, cur_freq):
            for c in w:
                if c not in cur_freq:
                    return False
                if cur_freq[c] == 0:
                    return False
                cur_freq[c] -= 1
            return True
        
        def helper(idx):
            if idx == len(words):
                return 0
            
            # keep current word only if we have enough chars
            keep = 0
            if can_keep(words[idx], freq.copy()) is True:
                # update freq
                word_score = 0
                for c in words[idx]:
                    freq[c] -= 1
                    word_score += scores[c]
                keep = word_score + helper(idx+1)
                # backtrack
                for c in words[idx]:
                    freq[c] += 1
            
            # skip
            skip = helper(idx+1)
            return max(keep, skip)
        
        return helper(0)
                