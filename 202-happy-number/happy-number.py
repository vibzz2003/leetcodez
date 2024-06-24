class Solution:
    def isHappy(self, n: int) -> bool:
        #base case
        if n==1:
            return True
        
        visited = set() #to keep check of unhappy numbers for not getting into a loop

        while n!=1:
            total = 0
            while n>0:
                digit = n%10
                total+=digit**2
                n //=10

            #if sum is in visited set that means we are in a cycle
            if total in visited:
                return False
            
            #otherwise add the sum in set
            visited.add(total)

            n = total
        
        return True