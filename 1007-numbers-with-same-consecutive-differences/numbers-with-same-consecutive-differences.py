class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = set()

        def backtrack(curr_num, last_digit, remaining_digit):

            #base case
            if remaining_digit == 0:
                result.add(curr_num)
                return
            
            next_digits = []
            
            if last_digit + k <= 9:
                next_digits.append(last_digit+k)
            
            if last_digit - k >= 0:
                next_digits.append(last_digit-k)
            
            for next_digit in next_digits:
                backtrack(curr_num*10 + next_digit, next_digit, remaining_digit - 1)
        
        for i in range(1, 10):
            backtrack(i, i, n-1)
        
        return sorted(result)

