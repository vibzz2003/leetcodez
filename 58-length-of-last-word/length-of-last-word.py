class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        #trim trailing spaces
        s = s.strip()
        #spliting the string by spaces
        words = s.split()

        if words:
            return len(words[-1])

        return 0
