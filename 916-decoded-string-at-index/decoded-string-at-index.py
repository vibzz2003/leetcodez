class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_len = 0

        for char in s:
            if char.isdigit():
                decoded_len *= int(char)
            else:
                decoded_len += 1
        
        for i in range(len(s)-1, -1, -1):
            current_char = s[i]

            if current_char.isdigit():
                decoded_len //= int(current_char)
                k %= decoded_len
            else:
                if k==0 or decoded_len == k:
                    return current_char
            
                decoded_len -= 1
    
        return ""