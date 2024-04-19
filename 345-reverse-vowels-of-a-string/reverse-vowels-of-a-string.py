class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        list1 = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        for i in range(len(list1)):
            if list1[i] in vowels:
                stack.append(list1[i])
                list1[i] = 0
            else:
                continue
        
        while len(stack)>0:
            for i in range(len(list1)):
                if list1[i] == 0:
                    list1[i] = stack.pop()

        str1 = ''.join(list1)
        return str1
