class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1 = {}
        for char in ransomNote:
            if char in hash1:
                hash1[char]+=1
            else:
                hash1[char]=1
        
        for char in ransomNote:
            if char not in magazine or hash1[char] > magazine.count(char):
                return False

        return True
            