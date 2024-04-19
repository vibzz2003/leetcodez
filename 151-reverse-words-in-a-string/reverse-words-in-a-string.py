class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        list2 = list1[::-1]
        str1 = ' '.join(list2)
        return str1