class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        size = len(nums)
        if size==1:
            return nums[0]
        maxavg = sum(nums[:k])/k  # Initialize maxavg to negative infinity
        winsum = maxavg*k

        for i in range(k, size):
            winsum += nums[i] - nums[i-k]
            maxavg = max(maxavg, winsum/k)
        
        return maxavg

