class Solution:
    def findComplement(self, num: int) -> int:
        loop = 0
        res = 0
        while num!= 0:
            a = (num & 1) ^ 1
            res += a<<loop
            loop+=1
            num = num >> 1
        return res