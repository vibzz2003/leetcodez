class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        size = len(nums)
        _sum = 0
        maxavg = float('-inf')  # Initialize maxavg to negative infinity
        for i in range(size):
            if k != 0:
                _sum += nums[i]
                if i >= k - 1:
                    maxavg = max(maxavg, _sum / k)
                    _sum -= nums[i - k + 1]
            else:
                maxavg = max(maxavg, nums[i])
        return maxavg

