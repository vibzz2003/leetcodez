class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Convert list to set for fast lookups
        memo = {}  # Memoization dictionary

        def can_break(start: int) -> bool:
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            word = ""
            for i in range(start, len(s)):
                word += s[i]
                if word in word_set and can_break(i + 1):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False

        return can_break(0)
