class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        size1 = len(word1)
        size2 = len(word2)
        hashmap1 = {}
        hashmap2 = {}

        if size1!=size2:
            return False
        else:
            for num in word1:
                if num in hashmap1:
                    hashmap1[num]+=1
                else:
                    hashmap1[num]=1
            
            for num in word2:
                if num in hashmap2:
                    hashmap2[num]+=1
                else:
                    hashmap2[num]=1
            
        if set(word1) != set(word2):
            return False
        
        return sorted(hashmap1.values()) == sorted(hashmap2.values())
            
