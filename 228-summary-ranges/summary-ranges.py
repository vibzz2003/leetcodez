class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                result.append(f"{start}->{nums[i-1]}" if start != nums[i-1] else f"{start}")
                start = nums[i]
        
        result.append(f"{start}->{nums[-1]}" if start != nums[-1] else f"{start}")
        
        return result