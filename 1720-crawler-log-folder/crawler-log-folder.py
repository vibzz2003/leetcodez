class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        count = 0
        for num in logs:
            if num != "../" and num != "./":
                stack.append(num)
            if num == "../" and len(stack)!= 0:
                stack.pop()
            if num == "./":
                continue
        
        while len(stack) != 0:
            stack.pop()
            count+=1
        
        return count