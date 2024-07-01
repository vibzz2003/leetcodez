class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0

        start = 0
        current_length = 0

        #map to check the count of values -> we store the most recent value at which the key occurs
        map1 = {}

        for end in range(len(s)):
            if s[end] in map1 and map1[s[end]]>=start:
                start = map1[s[end]] + 1
            map1[s[end]] = end
            current_length = max(current_length, end-start+1)

        return current_length