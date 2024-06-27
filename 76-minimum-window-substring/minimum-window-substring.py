class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        required_chars = Counter(t)
        missing_char = len(t)
        min_len, start = float('inf'), 0

        left = 0
        for right, char in enumerate(s, 1):
            if required_chars[char] > 0:
                missing_char -=1
            required_chars[char] -= 1

            if missing_char == 0:
                while required_chars[s[left]]<0:
                    required_chars[s[left]]+=1
                    left+=1

                window_len = right - left
                if window_len < min_len:
                    min_len = window_len
                    start = left

                required_chars[s[left]]+=1
                missing_char+=1
                left+=1

        return s[start:start + min_len] if min_len != float('inf') else ""