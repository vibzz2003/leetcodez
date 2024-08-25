class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        elif n<1:
            n = -n
            x = 1/x
            return self.myPow(x,n)
        else:
            mid = n//2
            b = self.myPow(x, mid)
            result = b*b
            if n%2==0:
                return result
            return result*x