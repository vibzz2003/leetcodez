class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxcount = float('-inf')
        dict1 = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        list1 = list(s)
        for char in list1[:k]:
            if char in dict1:
                count+=1
        maxcount = max(maxcount, count)
        
        for i in range(k, len(list1)):
            if list1[i] in dict1:
                count+=1
            if list1[i-k] in dict1:
                count-=1
            maxcount = max(maxcount, count)
        
        return maxcount
