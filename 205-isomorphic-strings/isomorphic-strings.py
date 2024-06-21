class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        hash1 = {}
        seen = set()

        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]

            if char1 in hash1:
                if hash1[char1]!=char2:
                    return False
            else:
                if char2 in seen:
                    return False
                hash1[char1]=char2
                seen.add(char2)
        return True
