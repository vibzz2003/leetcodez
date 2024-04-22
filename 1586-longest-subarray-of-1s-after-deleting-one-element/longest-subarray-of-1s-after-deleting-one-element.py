class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        size = len(nums)
        winsize = 0
        zero_count = 0

        for right in range(size):
            if nums[right] == 0:
                zero_count+=1
            
            while zero_count>1:
                if nums[left] == 0:
                    zero_count-=1
                left+=1
            
            winsize = max(winsize, right-left)

        return winsize
