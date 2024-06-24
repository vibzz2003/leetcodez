class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #use of split as it converts string in list
        hash1 = {}
        seen = set()
        words = s.split()

        if len(pattern)!=len(words):
            return False
        
        for char1, word in zip(pattern, words):
            if char1 in hash1:
                if hash1[char1]!=word:
                    return False
            else:
                if word in seen:
                    return False
                hash1[char1] = word
                seen.add(word)
        return True