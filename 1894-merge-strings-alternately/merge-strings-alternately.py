class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #[a,b,c,d] and [e,f,g,h]
        #[a]
        #[a,e]
        #[a,e,b] and so on...
        array1 = list(word1)
        array2 = list(word2)
        list1 = [] 
        for char1, char2 in zip(array1, array2):
            list1.append(char1)
            list1.append(char2)

        list1.extend(array1[len(array2):])
        list1.extend(array2[len(array1):])

        str1 = ''.join(list1)
        return str1
