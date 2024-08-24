class Solution:
    def bitwiseComplement(self, n: int) -> int:
        loop = 0
        res = 0
        if n == 0:
            return 1
        while n!= 0:
            a = (n & 1) ^ 1
            res += a<<loop
            loop+=1
            n = n >> 1
        return res