class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = {')':'(', '}':'{', ']':'['}

        if len(s)==1:
            return False

        for char in s:
            
            if char in bracket_pair.values():
                stack.append(char)
            if char in bracket_pair.keys():
                if not stack or stack.pop() != bracket_pair[char]:
                    return False
        
        if not stack == []:
            return False
        return True
        