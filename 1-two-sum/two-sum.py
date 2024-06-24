class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in hash1:
                return [hash1[complement], i]
            else:
                hash1[num]=i
        return []
