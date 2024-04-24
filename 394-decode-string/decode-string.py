class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr_string = ''

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((curr_string, num))
                curr_string = ''
                num = 0
            elif char == ']':
                prev_string, repeat = stack.pop()
                curr_string = prev_string + curr_string * repeat
            else:
                curr_string += char

        return curr_string