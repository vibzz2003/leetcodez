class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return -1
        
        index = haystack.find(needle)
        return index