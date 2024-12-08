class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result = ""
        result1 = ""
        for s1 in word1:
            result += s1
        
        for s2 in word2:
            result1 += s2

        print(result)
        print(result1)
        
        return result == result1