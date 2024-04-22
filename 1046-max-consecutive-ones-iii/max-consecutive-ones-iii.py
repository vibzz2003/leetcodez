class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxcount = float('-inf')
        size = len(nums)
        winsize = 0
        left = 0
        
        for right in range(size):
            if nums[right] == 0:
                winsize +=1
        
            while winsize > k:
                if nums[left] == 0:
                    winsize-=1
                left +=1

            maxcount = max(maxcount, right-left+1)

        return maxcount